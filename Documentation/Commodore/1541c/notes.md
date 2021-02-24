Ray Carlons 1541c.txt
```						
                             CBM 1541C       
                 latest updates and corrections 2-15-17 

     The 1541C is a cost reduced version of the earlier 1541 disk drive, 
but is identical in its basic functions. This drive uses single-sided 
double density disks. High density disks will NOT work. The short board 
251854 is unique to this last "standard" 1541 and has fewer, more 
integrated chips. Like the 1541-II, it has a single DOS ROM, 251968-01 
or -02. It also has a photo-sensor zero stop like the 1571 but that
sensor was disabled at the factory due to compatibility issues. The DOS 
ROM code in this drive makes the stepper go to track zero and chatter as 
it hits the mechanical stop on power up and with computer resets. This 
"feature" was installed by Commodore to eliminate a common problem with 
all 1541 drives... the drive getting "lost" past the directory track 
with its subsequent no-read symptom. An Initialize or Format would 
restore normal operation as would opening the drive and pushing the
head back, but such a drive might look defective to the user since 
turning it off and back on again does not restore normal operation.
     One other feature of the 1541C is the spindle motor enabled when 
a disk is inserted, much like a 1571, and it runs for several seconds 
afterwards. The write protect sensor triggers the motor so disk access 
is faster. 
     If it is desired to re-enable the sensor to eliminate the chatter 
at startup and reset, the user can cut jumper J3 near the large plug-in 
connector at the edge of the board. The jumper resembles a fat letter H 
and the tiny dash between the ends can be cut with a knife. I don't know 
how this change will affect other drive functions. User beware!
     A better way to eliminate the start-up chatter is to replace the
original DOS ROM 251968-01 or -02 with one from a 1541-II: 251968-03. 
Note that CMD's JiffyDOS uses the same code for both drives. Note that
changing the DOS ROM to the later one will not prevent stepper chatter
on Formats, Initialize, disk errors and some copy protected programs.   
     This drive is housed in a white case but not all 1541 drives in a 
white case are true C drives, only the ones with the short board. 
Commodore apparently used whatever hardware was available when building
their disk drives. Some will have Newtronics (twist door mechanism) and
others will have the older ALPS (push-down door) mechanism. Any drive 
that has the photo zero stop sensor will normally have it disabled.
     This design is what Commodore called "cost reduced" because it uses 
fewer, more integrated and some proprietary ICs. A reduced chip count 
can make troubleshooting more difficult and also makes finding some 
replacement chips difficult. Fortunately, most of the chips are 
interchangeable with earlier 1541 models. Exceptions are as follows:
     The R/W head amplifier chip UD1 is an LSI (large scale integration) 
with a non-Commodore number of H36A2U57. The one in a 1571 has the same 
number with a suffix D... I don't know if they would sub for each other. 
The gate array IC UC4 is the same as in a 1571: 251828-01. Other chips 
match the earlier 1541 drives and most large chips are socketed. 
     This drive has no device select switches but just jumpers on the 
controller board, namely J1 and J2 at the board edge. Like the 1541, the 
1541C uses two on-board power supply sources: +5VDC for the chips and 
+12VDC for the motors. 

                         THE DRIVE MECHANISM

     I've only seen one mechanism in a true C drive, Mitsumi (actually a 
Newtronics chassis). The Mitsumi reminds me of a 1571 mechanism but the 
single fixed head in this drive of course eliminates one of the weak 
points of the 1571, namely the flimsy top head mount. It does share one 
other failure point however... the door latch pin that works loose and 
falls out. When that happens, the door latch doesn't work and the lever 
just flaps loosely back and forth. If the pin is heard rattling around 
inside the drive (hopefully it hasn't shorted anything out), it can be 
reinserted in the door latch and secured with a dab of superglue. The 
Mitsumi mechanism has a spindle drive belt like earlier 1541 types and has 
a motor speed control on the drive PC board. 
     Maintenance for any drive should begin with cleaning of the head (use
alcohol or other solvent on a cotton swab) and stepper rails if they appear 
to be sticky. Before any other maintenance, if there is a buildup of dust 
inside the drive, blow it out with compressed air. Pay attention to the IR 
sensor near the front left side of the drive. That sensor signals the drive 
that a disk has been changed, and if clogged with dust, it may not report a 
disk change. That could corrupt the next disk inserted and written to in the 
drive. 
     The head gap is so tiny, you may not be able to see the residue that 
keeps your drive from reading disks reliably. It's best to just clean it 
every few months if the drive is used regularly and more often if your disks 
have seen a lot of use. It is not dirt that contaminates a head but oxide 
from worn disks. Make sure the felt pressure pad is intact on the upper 
spring loaded plate. If missing, you can replace it with a pad from an old 
audio cassette that has been trimmed to fit. Glue it with contact cement. 
     The stepper rails are the two metal bars that the head assembly slides 
back and forth on. Swab the rails with solvent and, either run them dry or 
apply a very light coat of sewing machine oil. Don't use any kind of spray 
lube inside the drive. Spray instead on a cotton swab, then apply to the 
rails. Plain oil tends to collect dust and gets sticky over time. A very 
light application of silicone spray on a Q-tip applied to the rails would 
work better and last longer than any kind of grease or oil. 
     Suspect a drive alignment problem -only- if the drive can't load known 
good programs (commercial disks) but it works fine with it's own recently 
formatted disks. A slightly misaligned drive will chatter when loading 
programs as it encounters disk read errors, and it will fail to load if 
severely misaligned. Note that some commercial programs have intentional 
errors as copy protection on the disk(s) that will make a normal drive 
chatter and flash the green LED while loading. 
     The 1541C can be "sluggish" and look like it's out of alignment but
it's usually caused by sticky head rails. Any 1541 drive can become 
sluggish if it sits for a long time without being used. The head assembly 
should slide back and forth easily (drive turned off, of course). If rails 
are sticky, the head has trouble finding the correct track quickly enough 
and you end up with intermittant read errors, especially when the drive is 
cold and seeks are at the outer tracks. 
     If your computer setup or components have been moved recently, take 
note: disk drive and serial cables too close to a tube TV or monitor can 
sometimes pick up interference from the flyback transformer in the display 
and garble the data. Move the drive and cables at least a foot away from 
the monitor and try it again. If that helps, move the drive to the other 
side of the monitor and route the cables away from the source of the
interference. 

IMPORTANT NOTICE: 
     If you remove the mechanism from the drive, mark the connectors so 
you will be sure to put them back correctly. Pin 1 is indicated on the 
board for each one. If accidentally reversed, you can do serious damage 
to the drive board or mechanism. Even though the black head connector is "keyed", if connected incorrectly, the hard-to-get R/W head amplifier 
chip may be destroyed!!! 

       CHIP FAILURES AND POSSIBLE SYMPTOMS - 251854 SHORT BOARD

UA1	7406		LOGIC
     No drive reset from computer or "Searching for..." but no further 
response from drive. See also UB1

UA2	251968-01 OR -02 DOS ROM, (reads as 27128 EPROM)
     Spindle motor runs continuously and red LED stays on or blinks. 

UA3	LC-3517A	SRAM (generic 6116 2K SRAM)
     When drive powered up, motor runs continuously and red LED flashes 
slowly (about 1 flash every 2 seconds). 

UB1     74LS14          LOGIC
     No response from computer
     
UC1	6522		VIA
     Drive appears to start up normally but does not respond to commands 
from computer or "Searching for..." but no further response from drive.

UC2	6502		MICROPROCESSOR
     Spindle runs continuously with red activity LED on.

UC3	6522		VIA
     Spindle motor runs continuously with no red LED, or spindle doesn't 
turn.

UC4	251828-0	GATE ARRAY 
     Spindle motor doesn't turn, or write protect not working, or stepper 
doesn't move.

UC5     251829-01       GATE ARRAY 
     

UC6     7406            LOGIC
     No drive reset, spindle motor run continuously

UD1     251853-02 (GENERIC H36A2U57)  HEAD AMPLIFIER LSI
     Read and/or write failure

UD2     TD308CD/TD1145C MASTER OSCILLATOR


                  DIAGNOSTICS... WHAT TO LOOK FOR

     When you are troubleshooting a drive, it is important to know how it 
works normally, and to observe it closely (with the cover off) for symptoms. 
For example, note how the drive motors and indicator LED's function when 
the drive is powered up, reset, and accessed by the computer. When the 
drive is instructed to LOAD a program, note whether the stepper moves, how 
much it moves, and if it "chatters". Try various functions like Initialize 
and Format, and observe the results. Sometimes the clues to a malfunction 
are subtle and different chips can cause the same apparent symptoms. Such 
things as a bad serial cable can be swapped out, but if another cable is 
not available, an ohmmeter check from one end to the other should show all 
pins connected. It's a "straight-through" cable: pin 1 to pin 1, 2 to 2, 
etc. with no shorts between adjacent pins. 
     If your drive suddenly goes "dead" and you can't read disks without 
"FILE NOT FOUND" errors, try Formating a disk or the Initialize command:
OPEN15,8,15:PRINT#15,"I0":CLOSE15 (assuming drive is set as device 8). 
This or formatting a disk will return the heads to track zero and may
bring it "back to life". The problem is a quirk in the operating system. 
It's the symptom the DOS ROM in the 1541C was "upgraded" to eliminate. 
If the drive encounters certain errors while running a program, or if the 
drive is turned off before a program is properly closed, the drive head 
may get "stuck" past the directory track. A computer reset or turning the 
drive off and back on again will not reset that condition, but an 
Initialize or disk format will return the heads and restore normal 
operation. As an alternative, if this happens and you have a program in 
memory that you don't want to lose, turn off the drive, take the top off 
and push the head back gently with your fingers. 
     To properly diagnose a potential problem, you have to know exactly 
how the drive should respond when it's working correctly.
 DRIVE POWER UP: Green power LED comes on and stays on, red activity LED 
comes on (and spindle motor turns) for about two seconds, then red LED 
should go out and motor should stop. With an original 1541C DOS ROM, the 
stepper will chatter on power up and computer resets. 
 COMPUTER POWER UP (OR RESET): Red LED should come on and go out, and 
spindle motor should start and stop within two seconds. 
 READ DIRECTORY: Insert a known good disk and type: LOAD"$",8 and hit the 
RETURN key. The disk should spin and the head should move forward to track 
18 and read the directory. The screen will show: SEARCHING FOR $. If it 
finds it, the screen will say READY within a few seconds (time delay 
determined by size of directory). If the disk read fails for any reason 
(drive door open, unformatted disk, bad chips in the drive, etc.), the 
red LED will flash and an error message: FILE NOT FOUND will appear. If 
you read the disk error channel, it will say: 74, DRIVE NOT READY,00,00. 
Note that you must "clear" the error by reading the error channel or 
resetting the drive, or subsequent read attempts will also fail. 
 INITIALIZE: This command from the computer should move the head from 
wherever it was to track 18 (directory) and the disk should spin. The head 
will not move (but the spindle motor will turn) if it is already over track 
18. If there is no disk in the drive, or you insert an unformatted disk, or 
if the drive door is open, it should cause the spindle motor to run and the 
head to seek track 18 (directory) anyway. When it tries and fails, it will 
pull the head back to track zero and "chatter" as it hits the head stop, 
then advance to where track 18 should be. The red LED will flash because 
of the drive read error. No error message will be shown on the screen, but 
if you read the disk error channel, it will say: 21,READ ERROR,18,00.
 FORMAT OR DISK "NEW": When you format a disk, the spindle motor will turn 
and the red LED will come on. The drive will pull the head back to track 
zero and "chatter", then the stepper will advance to each track as it writes 
from track 1 to track 35. When it finishes the format (about 1 minute 25 
seconds on a stock drive), the head will return to track 18 (directory). 
If the format fails, the red LED will flash, but there will be no error 
message on the screen. If you read the drive error channel, it will say: 
21,READ ERROR,00,00. Format failures can be caused by write protect, drive 
door open, bad disk, bad or clogged head, or bad chips in the drive. The 
format will attempt to write to track 1, then do a read, and if that read 
fails, the format will terminate, and the head will not move from track 1. 
If it advances a few tracks and stops, suspect a bad disk, an intermittant 
connection to the head or a faulty IC on the board. Swap out the drive 
mechanics to check the head. It may test good with an ohmmeter (not open 
circuit), but if defective, may still fail to format a disk. For write 
protect problems, check the sensor to see if dust or perhaps a loose write 
protect tab from an old disk is blocking it. 
     As mentioned above, it is sometimes helpful to read the disk drive 
error channel when the red activity LED is flashing. Here is a small 
BASIC program to do that. It reads the channel, displays the error message, 
and turns the flashing LED off. All of the possible drive error messages 
are listed in the back of the operators manual. 
 10 OPEN 15,8,15 
 20 INPUT#15,EN,EM$,ET,ES 
 30 PRINT EN,EM$,ET,ES 
 40 CLOSE 15


Ray Carlsen CET
Carlsen Electronics... a leader in trailing-edge technology.
```