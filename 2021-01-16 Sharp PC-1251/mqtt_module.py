import paho.mqtt.client as mqtt
import json
import time
from uuid import uuid4
import logging

logger = logging.getLogger(__name__)


class Module:
    def __init__(self, *, name, description):
        self._module_name = name
        self._module_description = description

        self._commands = {}
        self._topics_in = []
        self._topics_out = []

    def connect(self, *args):
        """Connect to the mqtt broker, make sure to call Module.register and Module.topic first."""
        # First check if any commands or topics are registered
        if len(self._commands) == 0:
            raise RuntimeError('No commands registered before starting MQTT')
        if len(self._topics_in) == 0:
            raise RuntimeError('No IN topics registered before starting MQTT')
        if len(self._topics_out) == 0:
            raise RuntimeError('No OUT topics registered before starting MQTT')

        # Connect to the MQTT broker and start the loop
        self._mqtt = mqtt.Client()
        self._mqtt.on_connect = self._on_connect
        self._mqtt.on_message = self._on_message
        self._mqtt.connect(*args)
        self._mqtt.loop_start()

        # Send the registration message
        self._last_registration_uuid = self._send_registration()
        self._last_registration_time = time.time()

    def register_in_topic(self, topic):
        """Register a topic to listen to."""
        self._topics_in.append(topic)

    def register_out_topic(self, topic):
        """Register a topic to publish to."""
        self._topics_out.append(topic)

    def register_command(self, *, callback, command, description, example, minimum_arguments=0, preformatted=False):
        """Register a command, this should be done before connecting, the server will not be updated."""
        # This is just a wrapper around the Command class
        self._commands[command] = Command(
            callback=callback,
            command=command,
            description=description,
            example=example,
            minimum_arguments=minimum_arguments,
            preformatted=preformatted
        )

    def _send_registration(self):
        # Base JSON for registration message
        data_dict = {
          "message_type_name": "registration",
          "message_type_version": 1,
          "message_time_stamp": time.time(),
          "message_uuid": str(uuid4()),
          "module_name": self._module_name,
          "module_description": self._module_description,
          "module_accepted_commands": {}
          }

        # Add each registered command
        for cmd in self._commands.values():
            data_dict["module_accepted_commands"][cmd.command] = {
                "description": cmd.description,
                "example": cmd.example,
                "minimum_arguments": cmd.minimum_arguments
            }

        # Only publish the registration message in the first registered topic.
        self._publish(data_dict)

        # Return the message UUID for verification
        return data_dict["message_uuid"]

    def _send_alert(self, alert_group, message):
        # Convert the message to a list if only a string is provided
        if isinstance(message, str):
            # Even if no newlines are present, this will still create a list.
            message = message.split("\n")

        # Base JSON for alert message
        data_dict = {
          "message_type_name": "alert",
          "message_type_version": 1,
          "message_time_stamp": time.time(),
          "message_uuid": str(uuid4()),
          "module_name": self._module_name,
          "alert_group": alert_group,
          "alert_message": message
         }

        # Publish the alert to all topics.
        self._publish(data_dict)

        # Return the message UUID for verification
        return data_dict["message_uuid"]

    def _send_response(self, results, uuid):
        # Convert the message to a list if only a string is provided
        if isinstance(results, str):
            # Even if no newlines are present, this will still create a list.
            results = results.split("\n")

        # Base JSON for alert message
        data_dict = {
          "message_type_name": "response",
          "message_type_version": 1,
          "message_time_stamp": time.time(),
          "message_uuid": uuid,
          "module_name": self._module_name,
          "results": results
         }

        # Publish the alert to all topics.
        self._publish(data_dict)

    def _on_connect(self, client, userdata, flags, rc):
        logger.info("Connected with result code "+str(rc))
        for topic in self._topics_in:
            client.subscribe(topic)

    def _on_message(self, client, userdata, message):
        text = message.payload.decode()
        logger.debug(f"Received message: {text}")
        # Make sure that the message is JSON
        try:
            output = json.loads(message.payload.decode())
        except BaseException:
            logger.debug("Unable to decode JSON of received messsage")
            return
        # Confirm the basic format:
        if not (output.get("message_type_name")
                and output.get("message_type_version") == 1
                and output.get("message_time_stamp")
                and output.get("message_uuid")):
            logger.debug("Incorrect arguments provided")
            return
        # Check if the message can be handled
        if output["message_type_name"] == "acknowledge":
            self._acknowledge_received(output)
        elif output["message_type_name"] == "command":
            self._command_received(output)
        elif output["message_type_name"] == "request_registration":
            self._last_registration_uuid = self._send_registration()
            self._last_registration_time = time.time()
        else:
            logger.debug("Message was neither an ack nor a command, ignoring it")

    def _acknowledge_received(self, message):
        # Confirm if the message is valid:
        if not message.get("acknowledgement_type") and message.get("acknowledgement_parameter"):
            logger.debug("Missing required parameters for a acknowledge, ignoring message")
            return
        # Check if this is the UUID we've been waiting for. In the future this should be expanded
        if not message["message_uuid"] == self._last_registration_uuid:
            logger.debug("Acknowledgement was not expected, ignoring it")
            return
        # Check and report the acknowledgement_type
        if message["acknowledgement_type"] == "ERROR":
            logger.error(f"Received ERROR acknowledgement from server with "
                         f"message: {message['acknowledgement_parameter']}")
        if message["acknowledgement_type"] == "OK":
            logger.debug(f"Received GOOD acknowledgement from server with "
                         f"message: {message['acknowledgement_parameter']}")
            logger.info("Successfully registered with server")
        else:
            logger.error(f"Received unknown acknowledgement: {message['acknowledgement_type']} "
                         f"from server with message: {message['acknowledgement_parameter']}")

    def _command_received(self, message):
        # Confirm if the message is valid:
        if not (isinstance(message.get("module_name"), str)
                and isinstance(message.get("command"), str)
                and isinstance(message.get("parameters"), list)
                ):
            logger.error("Missing required parameters for command, ignoring message")
            return
        command = message["command"]
        parameters = message["parameters"]

        if not message["module_name"] == self._module_name:
            logger.debug("Command is not meant for me, ignoring")
            return
        if command not in self._commands:
            # IMPROVEMNT - This requires an ERROR ack
            logger.error("Received unknown command for this module")
            return
        if not len(parameters) >= self._commands[message["command"]].minimum_arguments:
            # IMPROVEMNT - This requires an ERROR ack
            logger.error("Insufficient arguments received for command")

        # Run command
        result = self._commands[command].callback(command, parameters)
        if not result:
            return False
        if self._commands[command].preformatted:
            result = ["```", *result, "```"]
        self._send_response(result, message["message_uuid"])

    def _publish(self, message):
        for topic in self._topics_out:
            self._mqtt.publish(topic, json.dumps(message, indent=4))


class Command:
    def __init__(self, *, command, callback, description, example=False, minimum_arguments=0, preformatted=False):
        self.command = command
        self.callback = callback
        self.description = description
        self.example = example
        self.minimum_arguments = minimum_arguments
        self.preformatted = preformatted
