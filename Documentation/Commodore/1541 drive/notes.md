# Service manuals and schematics

[Full service manual](1541 service manual HTML/SERVIC~1.HTM) - Source: http://www.cbmhardware.de/314002/index.php

# Ray Carlsen documents

### fix1541.txt

[Original](http://personalpages.tds.net/~rcarlsen/cbm/1541/fix1541.txt)

```
			       1541 DIAGNOSTICS
	    Some symptoms and solutions for a sick disk drive. 
               latest updates or corrections: 3-7-2017

 WHEN THE DRIVE IS WORKING PROPERLY
										
     To properly diagnose a potential problem, you have to know exactly how 
the drive should respond when it's working correctly. Before you start, if the
drive has sat unused for a long time, you might want to check a few things 
before you power it up. On an ALPS (push-down door) mechanism, the head 
assembly should move back and forth (drive off) easily with your finger. If 
it is hard to move, the rails should be cleaned. ALPS drives seem to suffer 
more from sticky rails than Newtronics mechanisms. The stepper assembly in a 
Newtronics (twist-down door) mechanism is normally harder to move with a 
finger, and it is less likely to suffer from sticky rails. Clean the head 
while you have the drive open. Here's how, after removing the drive top cover 
(4 screws in the case bottom) and the metal shield (two screws) over the PC 
board. To clean the head, use a Q-tip cotton swab moistened with alcohol to 
gently wipe the head surface after raising the pressure pad out of the way. 
If the head clog is very stubborn, you can use a pencil eraser (a very fine 
but gentle abrasive) to rub the head clean. I'll include a closeup photo, 
before and after cleaning. Make sure the head is dry before inserting a disk. 
Never spray anything into a disk drive but compressed air can be used to blow 
the dust out. Cleaning the stepper rails will be described later. 

 DRIVE POWER UP: Green power LED comes on and stays on, red activity LED comes 
on and spindle (which turns the disk) motor runs for about two seconds, then 
red LED goes out and spindle motor stops. There is no stepper (which moves the 
head assembly) motor activity at this time.
 COMPUTER POWER UP (OR RESET): Drive red LED should come on and spindle motor 
should start, then LED goes off and motor stops within two seconds.
 READ DIRECTORY: Insert a known good disk and type: LOAD"$",8 and hit the 
RETURN key. The disk should spin and the stepper should move the head to track 
18 and read the directory. The screen will show: SEARCHING FOR $. If it finds 
it, the screen will display READY. Then you can type LIST to see the contents 
of the disk. Note: some program disks will not have a directory you can list. 
If the disk read fails for any reason (drive door open, unformatted disk, bad 
chips in the drive, clogged R/W head, etc.), the drive stepper will gently 
"burp" four times (moves slightly back and forth), then the red LED will flash 
and an error message: FILE NOT FOUND will appear on the screen. If you read 
the disk error channel, it will display: 74, DRIVE NOT READY,00, 00.
 INITIALIZE: This command from the computer should move the head from wherever 
it was to track 18 (directory) and the disk should spin. The head will not move 
(but the spindle motor will turn) if it is already over track 18. If there is 
no disk in the drive, or you insert an unformatted disk, or if the drive door 
is open, INITIALIZE should cause the spindle motor to run and the head to seek 
track 18 (directory) anyway. When it tries and fails, it will pull the head 
back to track zero and "chatter" as it hits the head stop, then advance to 
where track 18 should have been. The red LED will flash because of the drive 
read error. No error message will be shown on the screen, but if you read the 
disk error channel, it will display: 21,READ ERROR,18,00. More on this later...
 FORMAT OR DISK "NEW": When you format a disk, the spindle motor will turn 
and the red light will come on. The drive will pull the head back to track 
zero and "chatter", then the stepper will advance to each track as it writes 
from track 1 to track 35. With a "stock" drive, the steps are about two 
seconds apart. When it finishes the format (about 1 minute 25 seconds on a 
stock drive), the head will return to track 18 (the directory). If the format 
fails, the red activity LED will flash, but there will be no error message on 
the screen. Reading the drive error channel will display: 21,READ ERROR,00,00. 
Format failures can be caused by a write protect (disk tab on), drive door 
open, bad disk, bad or clogged head, or bad chips in the drive, in roughly 
that order of likelyhood. The format will attempt to write to track 1, then 
do a read, and if that read fails, the format will terminate, and the head 
will not move from track 1. If it advances a few tracks and then stops or 
takes a long time to format, suspect a bad disk or a partial head clog. 
     If a drive will read OK but fails to format a disk, check the head, UC1, 
UC2, UA1, and UD2. Swap out drive mechanics to verify the head is bad. It may 
test good with an ohmmeter and read disks OK, but if defective internally, 
may fail to format a disk. Note that all wires of the head should measure 
continuity (low resistance) to each other. If any line is open (pin #5 seems 
to be most common to open up in the Newtronics drive), the head is bad. 
Disconnect the plug from the drive to do the resistance tests and make sure 
you get the plug back on the connector the same way it came off. To do the 
resistance check, it's helpful to use straight pins to touch the connectors
on the side of the plug shell. 
     The twist-door Newtronics mechanisms seem to suffer a higher failure 
rate from an open R/W head than the push-down ALPS ones. I don't know why but 
I speculate that Newtronics didn't seal the heads well enough and moisture 
seeps in and corrodes the wiring. Storing a drive in a humid environment is 
therefore to be avoided. An open head is not repairable. I usually just swap 
out the entire mechanism. I did once substitute an ALPS head element into a 
Newtronics head assembly just to see if it would work... it did. However, 
that required the epoxy to be chipped away from both, without breaking them, 
and shims were needed to raise the height of the new head to match the old. 
     For write-protect problems, check UC1, UC2, UA1 and, of course, the 
sensor. Look for a stuck write protect tab that has fallen off a disk. If 
the drive is dusty inside, there could be some dirt inside the sensor. The 
spacing is tight, so a quick shot of "canned air" will take care of it. 
Note: if cleaning the head with solvent doesn't help, try rubbing it with a 
pencil eraser. It is a mild abrasive and will not hurt it. Try the read again. 
     As mentioned above, it is sometimes helpful to read the disk drive error 
channel when the drive red light is flashing. Here is a small BASIC program 
to do that. It reads the channel, displays the error message, and turns the 
red activity LED off. 
 10 OPEN 15,8,15 
 20 INPUT#15,EN,EM$,ET,ES 
 30 PRINT EN,EM$,ET,ES 
 40 CLOSE 15
This program and all of the possible drive error messages are listed in the 
back of the disk drive operators manual. Note that JiffyDOS provides an easy 
way to check the error channel... just press the @ key, then hit RETURN. 

 DRIVE DEAD... OR NEARLY

     Lets take it from the top. Does the drive start up properly when turned 
on? If the power light (green LED) doesn't come on, or is dim or flickers, you 
probably have a power supply problem... the 5 volt line is bad. That usually 
results in a spindle motor that runs continuously with red LED off. Check the 
bridge rectifier (CR3 in early version drives with PCB# 1540050, and CR1 in 
later version drives with PCB# 251830) and the 5 volt regulator VR2. Note: if 
the regulated 12 volt supply fails, the motors will not run at all. That's a 
rare failure but I've seen a few shorted tantalum caps (C15, 10uF 25V) pull 
that line down.
     At power up (without the computer connected) if the red activity LED 
stays on and the motor runs continuously, it means that the drive failed to 
complete its startup sequence. The most common causes are a bad DOS ROM UB4 
(901229-xx) or failing 5V bridge rectifier, but other bad chips can produce 
those symptoms. The easiest place to check for correct voltages in and out 
of the power supply regulators is at the diodes CR2 and CR4 located near the 
two rectifiers. The anodes of those diodes are connected to the outputs of 
the +5V and +12V regulators. The cathodes (designated by a line or stripe 
at one end) show the unregulated source from the rectifiers that feed the 
regulators... about 10V for the 5V source and 20V for the 12V source.
     With drive startup problems, some chips to check are: UC4 (6502 MPU) and 
UC2 (6522 VIA). The smaller "glue logic" chips are pretty rugged, but do 
sometimes fail. Check UA1 (74LS14) and UD2 (7407)... they have also been known 
to cause those symptoms.

 DRIVE POWERS UP OK, BUT WILL NOT LOAD THE DIRECTORY OR PROGRAMS

     When the computer is turned on, the reset signal from the computer should 
cause the drive (and other peripherals like the printer) to reset. The red LED 
and spindle motor should come on and go off within a few seconds. If that 
doesn't happen, try a substitute serial cable. If that's OK, suspect the 
interface chips in the computer or VIA chip in the drive. If the computer 
resets other peripherals, it's probably OK. Note that a drive may stay in reset 
(red LED on and spindle turning) if connected to a computer that is turned off. 
That's normal. Disconnect or turn on the computer to check.
     If the computer can't "see" the drive on the serial bus, (serial cable 
unplugged or drive turned off, for example) you will immediately get an error 
message: "DEVICE NOT PRESENT" when you try a LOAD command, and the red LED 
will start flashing. The default (factory setting) for a 1541 is device #8. 
If your drive is hardware modified as device 9 for example, and you try to 
read the directory with LOAD"$",8 you will get that error message but 
LOAD"$",9 will work. If the VIA (UC3) 6522 interface chip in the drive is bad, 
the drive will likewise be "invisible" to the computer and you'll get "DEVICE 
NOT PRESENT".

     If you get "SEARCHING FOR" and nothing else happens, check ICs UB1 (7406) 
and UA1 (74LS14). These two chips carry data to and from the VIA chip. When 
one of them fails, if you try to load the directory or a program, the computer 
will display that error message until you turn it off or reset it. 
 74,DRIVE NOT READY,00 00 from the drive error channel indicates the computer 
can "see" the drive on the serial bus, but 1. there is no disk in it, 2. the 
disk is not formatted, 3. the drive door is not closed, 4. the read/write head 
is completely clogged or 5. the drive has an electrical problem. With any of 
these problems, the drive head can't find -any- data. The drive will respond 
by flashing its red activity LED and may step the head back and forth slightly 
looking for data. Note that this takes only a second or two before the drive 
"gives up" and the spindle stops. 
     A partially clogged R/W head may allow the drive to see data but still 
not read it properly. Other similar false reads would include a corrupted 
disk or trying to load the directory of the reverse side of a 1571 formatted 
disk. In any case, if the drive can see data but can't read it properly, it 
takes some time "hunting" before it gives up trying... more time than if it 
doesn't see any data. That's an important clue. You may hear the head assembly 
"chatter" as it bangs against the head stop seeking track zero... a normal 
process if disk errors are encountered. 

 DRIVE SUDDENLY WILL NOT READ DISKS OR LOAD PROGRAMS

     One quirk of the 1541 is the "drive lost" symptom. Normally, the drive 
will "park" the head over the directory track (18). If the head, for some 
reason, stops past the directory track, an INITIALIZE command from the 
computer will return it to track zero and it should then work normally. Note: 
turning the drive off and back on again will -not- reset it if that's the 
problem! Some disk errors can do that to a drive and make it look "dead", 
as can exiting incorrectly from some programs by just turning off the 
computer. So, if the computer can access the drive, but you can't load even 
the directory of a known good disk, try the INITIALIZE command (with or 
without a disk inserted), then try reading A disk again. To INITIALIZE the 
drive:
 OPEN15,8,15 <return>
 PRINT#15,"I" <return>
 CLOSE15 <return>
As an alternative to Initializing, you could try formatting a disk. That will 
also return the head to track zero. Lastly, if you insert the original CBM 
transit card shipped with the drive (drive turned off) it will push the head 
back to track zero. Inserting a disk will not do it. The transit card has a 
tab on the front (the longer of the two tabs if there are two) that moves 
the head back. Don't have your transit card? With the top cover off and metal 
shield (if your drive has one) removed, you can push the head assembly back 
with your finger. The drive must be turned off, of course, or the head 
assembly may not move. The transit card is preferred to Initialize or Format 
as you don't have to turn off the computer (just the drive) so you don't lose 
a program in memory.
     One important note to make here is to avoid turning the drive on or off 
with a disk inserted. Whether or not the disk is write protected, it's a 
risk and sooner or later it will corrupt a disk and make it unreadable! 

 PROGRAMS FAIL TO LOAD COMPLETELY OR COMPUTER LOCKS UP

     If your computer setup or components have been moved recently, take note: 
drives or cables too close to a TV or monitor can sometimes pick up "noise" 
interference from the high voltage circuits inside the monitor which can garble 
the data. Move the drive and cables at least a foot away from the monitor and 
try it again. If that helps, move the drive to the other side of the monitor 
and keep the cables as far away as possible.
     If you have re-initialized the drive and it still doesn't work (can't
read a disk), it may be out of alignment. Keep in mind that actual alignment 
problems are not as common as once thought. Try formatting a disk and see if it 
can read the (empty) directory of that disk. If it can't, clean the head and 
try it again. If it can, but can't read other disks, then misalignment is a 
good possibility. There is one other thing you should check first: see if the 
head assembly rails are sticky, especially on a drive that has sat unused for 
a long time. With power off, the head assembly should slide back and forth 
easily and the tension band should be taut. It's kept in place with a spring 
but old grease can cause it to stick too far forward. If the rails seem sticky 
(experience helps to know the difference between good and bad), the rails 
can be cleaned with a drop of WD-40 on a Q-tip cotton swab. WD-40 is not a 
lubricant but it works well as a solvent to clean up the rails. Spray a small 
amount of solvent on a Q-tip (cotton swab) and then wipe the rails, work the 
head assembly back and forth, clean the rails again, and repeat as necessary 
until no more residue is found. I would avoid putting oil on the rails. It will 
work for a time, but it eventually picks up dirt and the rails will get sticky 
again. I run them "dry" or one can use a small amount of graphite based or 
silicone lube. Avoid the use of sprays directly into the drive. The spray goes 
everywhere and can contaminate the next disk you insert in the drive. 

 SOME ODD FAILURES

     If you smell or see smoke from your drive, of course turn it off quickly. 
OK, where did it come from? Look at all the tiny electrolytic capacitors (known 
in the trade as Tantalum) to see if any are burned. When new, they are orange 
or dark blue in color and shaped like a teardrop. Those capacitors have a 
history of catastrophic failure and can pop like a firecracker or just make a 
lot of smoke when they fail. I've seen them short out and drag the +12V line
down so the motors didn't work. The regulator IC's have an internal protective
feature called "fold-back current limiting, so they will not immediately burn 
out from an overload like that but the regulator and its supply rectifier 
will get very hot quickly. If the +12V line is lower than normal, suspect
a shorted C15, a 10uF 25V tantalum capacitor on the front of the board.
     Another odd failure I've seen is the spindle motor turning all the time, 
but the drive still works perfectly. The cause is a bad UD2, IC number 7407 or 
7417 (those are interchangeable parts). When just part of that IC fails, it 
keeps the spindle motor running, but with no other symptoms... strange as it 
seems. You have to listen closely to hear it, especially with no disk inserted.

 DRIVE ALIGNMENT

     Drive misalignment is something that doesn't usually happen all at once. 
It's normally a gradual process that begins with occasional disk errors (bad 
disk or intentional errors from copy protection) while loading (red LED 
flashing), failure to work with some programs, or excessive head chatter (the 
drive getting "lost" and having to go back to track zero to "find" it's place 
again.) Drives are forced out of alignment mostly while hot from extended use. 
Heavily copy protected programs or disk errors can cause the head to chatter 
against the track zero stop repeatedly. If the alignment is far enough off, 
you will get "FILE NOT FOUND" errors and red LED flashing with all disks, and 
the drive may try several times before "giving up". Note that misalignment 
will cause read errors with known good disks but such a drive will probably 
still be able to format a disk and read it back again. A disk formatted on a 
misaligned drive will not read properly on a correctly aligned drive. 
     To properly realign a drive, you need special software. I use "1541/1571 
Drive Alignment" by Free Spirit Software. The flipside of the program disk is 
the alignment disk, and as such, should not be copied. A copy is only as good 
as the drive that made it. The program provides a menu screen that indicates 
what track you're on, drive speed, etc. You make adjustments to the drive 
while watching the screen. The instructions even tell you how to load the 
program when nothing else will load. You can -check- the alignment of the 
drive without taking it apart, but of course realignment requires disassembly.
I always final-check my drives with several different program disks to verify 
alignment... any commercial program disk can be used to do that. 
     Drive speed can drift over time, but it's rather rare to find it off far 
enough to cause problems. Spindle speed (Note: some drives have no adjustment) 
is reset with a small screwdriver adjustable control on a small PC board near 
the spindle motor. On older belt-driven spindle motors, the belt may be 
slipping. On all drives, the spindle collar (clamper) can get sticky and a 
tiny bit of lube helps. Don't overdo lubrication. Excess oil will be thrown 
off and could get on the disks. 

 MISCELLANEOUS 

     Make sure the latch clamps the disk properly. Without a disk, move the 
lever down and see if the spring presses the collar against the spindle to 
clamp it securely. You can bend the tab down -slightly- (Newtronics drives 
only) so it makes more firm contact if necessary. A slipping or stalling 
disk will produce random read and write errors, a problem that's very hard 
to track down. Some disks may work better than others. The DD ones without a 
hub ring seem to slip more easily. HD disks should never be used in a 1541. 
     Bad (sticky) old grease on an ALPS drive can actually stall the spindle 
motor. If that is suspected, or the clamper is noisy, you can try a drop of 
oil in the center of the spindle clamper and run the drive to let the oil 
work its way in. If that doesn't help, you wiil have to remove the metal bar 
that the hub lock is mounted on (two screws in the back) and take apart the 
clamper assembly by removing the C clip. It has half a dozen assorted 
washers, a brass bushing and a spring along with the plastic hub. Don't allow 
any of the spring-loaded parts to fly off when you remove the C clip. These 
parts need to be cleaned with solvent and put back together in the same 
order as before. A bit of moly lube or light oil finishes the job. Make sure 
the hub clamper is centered on the spindle (drive door closed) before you 
fully tighten the its screws. 
     Another common problem with the ALPS (push-down door) mechansim is a
sticky latch. The symptom is usually that it will not pop out when the door 
is pressed down. The grease on the sides of the plastic latch gets sticky 
and makes the latch sluggish. A drop of oil on each side of the latch and 
"exercising" it to work the lube in will usually fix it. Be sure to wipe
up any excess. You don't want oil on your disks!
     If the Newtronics (twist door) mechanism stepper seems sticky after 
cleaning the rails, you can try adding a few drops of oil to its shaft by 
tipping the drive on its rear and applying the oil to the space between 
the stepper collar and the metal base. The oil will run down and collect 
on the shaft (without disassembly) and wick it's way into the bearing. The 
same thing can be done to quiet a noisy spindle, but I've had to take a few 
of those apart to replace a really noisy bearing. Don't overdo the oiling, 
and keep a rag handy to clean up the excess. 
     I made a survey of all the repair jobs I did on about 40 1541's. It 
might be helpful to know the number of bad chips I replaced to give you 
some idea of the statistics of the most common failures:
6502		CPU		6
6522		VIA		10	most often UC3
901229-05	DOS ROM 2	5
325302-01	DOS ROM 1	1
325572-01	MTR CTRL	1
7406		LOGIC		4
7407 (7417)	LOGIC		4
74LS14	LOGIC			1
311		COMPARITOR	1
BRIDGE RECTIFIER		4	either 5V or 12V source can drop out
TANTALUM CAPACITOR C15		3	can burn up or short and drop 12V power
BAD NEWTRONICS HEAD		16	ALPS head is a rare failure

Ray Carlsen CET
CARLSEN ELECTRONICS... a leader in trailing-edge technology.
Questions and comments are welcome, especially if you spot a mistake
here. Thanks!
```

### 1541chip.txt
[original](http://personalpages.tds.net/~rcarlsen/cbm/1541/1541chip.txt)

```

                        1541 CHIPS VS SYMPTOMS
                latest additions or corrections: 2-26-2017

     This list represents the most common versions of the 1541 in the 
standard brown case with PC board numbers 1540050 (early ALPS push-down 
door mechanism) and the 251830 and 251777 (Newtronics twist door 
mechanism).
     Although the very early "long board" (white case) 1541 is not 
represented here, major chip functions are of course similar. That drive 
used more TTL (so-called "glue logic") chips that were later "integrated" 
into a single motor control IC. Although functionally identical, newer 
drives such as the 1541C and 1541-II integrate more functions into fewer 
more specialized IC's, making some repair parts even harder to find.
      Although most of the chips in the different versions of the 
standard brown case 1541 are the same, board layout and some chip ID 
numbers may be different. To minimize confusion, I will list the two 
major versions of the drive separately. 
     In another article (fix1541.txt) I will offer some troubleshooting 
tips. Included is how the drive should behave during normal operation 
and what is likely to cause a particular fault. Before suspecting any 
IC chips, don't overlook more common causes of problems such as a dirty 
read/write head or sticky rails. Always check the "easy stuff" first 
such as clogged R/W head and swapping out socketed chips. 

  *****************************************************************

1541 CHIPS VS SYMPTOMS 
PCB# 1540050 (early version) with ALPS drive mechanism (1982) 

UA1 74LS14 LOGIC
  Partial failure common cause of "FILE NOT FOUND" error or fail to 
reset when computer is turned on. Total failure: when drive powered up, 
red LED stays on and spindle motor runs continuously (check also UB4, 
UC2, UC4, UC5, UC6, UD3, and UD5). 

UB1 7406 (M53206P) LOGIC
  Partial failure most common causing "SEARCHING FOR" (also check UC3), 
computer lockup or "DEVICE NOT PRESENT". Total failure: drive may power 
up normally, but will not reset when the computer is turned on. 

UB2 TMM2016AP-10 16K SRAM  also TMM2116AP-15 or MB8128-15
  When drive powered up, motor runs continuously and red LED flashes
slowly (about 1 flash per second). 

UB3 325302-01 DOS ROM 1
  When drive powered up, red LED flashes 2 or 3 times repeatedly. 

UB4 901229-03 or -05 DOS ROM 2
  When drive powered up, red LED stays on and spindle motor runs
continuously. DOS ROM is a common failure. Check also UA1, UC2, UC4,
UC5, UC6, UD3, and UD5.

UC1 325572-01 MOTOR CONTROLLER
  When drive powered up, red LED comes on and goes out, but spindle
motor does not turn. When LOAD attempted, spindle does not turn, red
LED flickers, screen displays "FILE NOT FOUND" and red LED flashes. 
Can also cause spindle to run when drive not accessed.

UC2 6522 VIA (MOTOR CONTROL INTERFACE) 
  When drive powered up, red LED stays on and spindle motor runs
continuously. Check also UA1, UB4, UC4, UC5, UC6, UD3, and UD5.

UC3 6522 VIA (SERIAL INTERFACE) 
  Drive powers up and resets normally. When LOAD attempted, screen
may indicate "SEARCHING FOR ...", but no motors run and red LED does 
not light. Computer will be locked up until reset or turned off.

UC4 6502 MPU
  When drive powered up, red LED stays on and spindle motor runs
continuously. Check also UA1, UB4, UC2, UC5, UC6, UD3, and UD5. 

UC5 74LS04 (74LS14) LOGIC
  When drive powered up, red LED stays on and spindle motor runs
continuously. Check also UA1, UB4, UC2, UC4, UC6, UD3, and UD5. 

UC6 74LS00 LOGIC
  When drive powered up, red LED stays on and spindle motor runs
continuously. Check also UA1, UB4, UC2, UC4, UC5, UD3, and UD5. 

UC7 74LS42P LOGIC (DECODER) 
  When drive powered up, motor runs continuously and red LED flashes
slowly (about 1 flash every 2 seconds). Red LED may stay on and/or
motor may stop. 

UD1 7406 (M53206P) LOGIC
  When drive powered up or reset, spindle motor runs momentarily, 
but red LED doesn't come on. When LOAD attempted, screen indicates
"SEARCHING FOR ..." but red LED does not light, spindle runs
continuously, and screen shows "FILE NOT FOUND"  error. Partial 
failure: no read, no stepper movement or just buzzes or chatters.

UD2 7407 or 7417 (M53207P or M53217P) LOGIC (R/W CONTROL BUFFER) 
  When drive powered up or reset, red LED comes on and goes out, but
spindle motor does not turn. If LOAD is attempted, red LED comes on,
stepper moves slightly, spindle doesn't turn, "FILE NOT FOUND" and 
red LED flashes. One failure causes motor to run all the time but 
the drive otherwise works normally. This IC can corrupt formats.

UD3 74LS86 LOGIC
  When drive powered up, red LED stays on and spindle motor runs
continuously. Check also UA1, UB4, UC2, UC4, UC5, UC6, and UD5. 

UD4 9602 (8602) LOGIC (MMV)  no sub with later board 74LS123!
  Drive powers up and resets normally, but if LOAD is attempted,
spindle motor runs with red LED out. Screen displays "SEARCHING FOR
..." and stepper does not move. Check also UE6.

UD5 74LS197 (74177) LOGIC (TIMER) 
  When drive powered up, red LED stays on and spindle motor runs
continuously. Check also UA1, UB4, UC2, UC4, UC5, UC6, and UD3. 

UE4 LM311 COMPARITOR (READ LOGIC)
  Powers up normally. When LOAD attempted, spindle turns and red LED
comes on, but "FILE NOT FOUND" and red LED flashes. Check also UF3
and UF4.

UE6 74LS193 LOGIC (BINARY COUNTER) 
  Drive powers up and resets normally, but if LOAD is attempted,
spindle motor runs with red LED out. Screen displays "SEARCHING FOR
..." and stepper does not move. Check also UD4.

UF3 NE592N READ PREAMPLIFIER
  Powers up normally. When LOAD attempted, spindle runs and red LED
comes on, but "FILE NOT FOUND" and red LED flashes. Check also UE4
and UF4.

UF4 NE592N READ AMPLIFIER
  Powers up normally. When LOAD attempted, spindle runs and red LED
comes on, but "FILE NOT FOUND" and red LED flashes. Check also UE4
and UF3.

VR1 UA7812KC (LM340KC-12) +12 VOLT REGULATOR
  Drive powers up "normally", but motors run slowly or not at all. 
If that happens, drive access will produce a flashing red activity
LED and errors "file not found" or "drive not ready" on the error 
channel. Also suspect an overload (shorted C15) on the supply line.

VR2 UA7805KC (LM340KC-5.0) +5 VOLT REGULATOR
  Green (power) LED dim, flickers, or does not come on at all, but
spindle may run continuously and red LED may be dark.

CR1  2 AMP 200V BRIDGE RECTIFIER (FOR +12V) 
  Drive appears to power up normally, but motors do not run. Should 
get warm only if the drive is being accessed (motors running). 

CR3  2 AMP 200V BRIDGE RECTIFIER (FOR +5V) 
  On power up, green and red LED's are dim or dark and spindle motor 
runs continuously. May be intermittant and "die" after warmup. Part 
runs very hot normally and is a common failure in this model.

******************************************************************

1541 CHIPS VS SYMPTOMS PCB# 251830 or 251777 with Newtronics drive
mechanism (1984)

UA1 74LS14 LOGIC
  Partial failure common cause of "FILE NOT FOUND" error. Total
failure: when drive powered up, red LED stays on and spindle motor 
runs continuously (check also UB4, UC2, UC4, UC6, UC7, UD3, and UD5). 

UB1 7406, 7416, M53206P or 7707 LOGIC
  Partial failure common cause of "SEARCHING FOR" (check also UC3)
and "DEVICE NOT PRESENT" errors. Total failure: drive powers up OK, 
but does not respond to computer... no reset or disk access. One 
failure can lock up computer until it is reset. 

UB2 TMM2016AP-10 16K SRAM  can be TMM2116AP-15 or MB8128-15
  When drive powered up, spindle motor runs continuously and red LED
flashes about once per second. 

UB3 325302-01 DOS ROM 1
  When drive powered up, red LED flashes 2 or 3 times repeatedly. 

UB4 901229-03 or -05 DOS ROM 2
  When drive powered up, red LED stays on and spindle motor runs
continuously. DOS ROM is a common failure. Check also UA1, UC2, UC4,
UC6, UC7, UD3, and UD5.

UC1 325572-01 MOTOR CONTROLLER
  When drive powered up or reset, red LED comes on and goes out, but
spindle motor does not turn. When LOAD attempted, spindle does not
turn, red LED flickers, screen displays "FILE NOT FOUND" and red LED
flashes. This IC can cause spindle to run without drive access.

UC2 6522 VIA (MOTOR CONTROL INTERFACE) 
  When drive powered up, red LED stays on and spindle motor runs
continuously. Check also UA1, UB4, UC4, UC6, UC7, UD3, and UD5.

UC3 6522 VIA (SERIAL INTERFACE) 
  Drive powers up and resets normally. When LOAD is attempted, 
screen may indicate "SEARCHING FOR ...", but no motors run and red 
LED doesn't light. Computer is locked up until turned off or reset.

UC4 6502 MPU
  When drive powered up, red LED stays on and spindle motor runs
continuously. Check also UA1, UB4, UC2, UC6, UC7, UD3, and UD5. 

UC6 74LS04 (7713) LOGIC
  When drive powered up, red LED stays on and spindle motor runs
continuously. Check also UA1, UB4, UC2, UC4, UC7, UD3, and UD5. 

UC7 74LS00 LOGIC
  When drive powered up, red LED stays on and spindle motor runs
continuously. Check also UA1, UB4, UC2, UC4, UC6, UD3, and UD5. 

UC8 74LS42 LOGIC
  When drive powered up, spindle motor runs continuously. Red LED 
may stay on, or flash three times and go out. 

UD1 7406 (M53206P) LOGIC
  When powered up, spindle motor runs momentarily, but red LED
doesn't come on. When LOAD attempted, screen indicates "SEARCHING 
FOR..." but red LED does not light and spindle runs continuously.
Partial failure: no read, stepper doesn't move or just buzzes or 
chatters. 

UD2 7407 or 7417 (M53207P or M53217P) LOGIC (R/W CONTROL BUFFER) 
  When drive is powered up or reset from computer, red LED comes 
on and goes out, but spindle motor does not turn. When LOAD is
attempted, stepper moves slightly, spindle doesn't turn, and error
message on screen is "FILE NOT FOUND" with flashing red LED. One 
failure causes motor to run continuously but drive works normally.
This IC can cause good reads but corrupted formats.

UD3 74LS86 LOGIC
  When drive powered up, red LED stays on and spindle motor runs
continuously. Check also UA1, UB4, UC2, UC4, UC6, UC7, and UD5. 

UD4 74LS123 LOGIC (MMV)  no sub with earlier board 9602 IC!
  Drive powers up and resets normally, but when LOAD is attempted,
screen indicates "SEARCHING FOR ..." red LED does not light and
spindle runs continuously. Check also UE6. 

UD5 74LS197 (74177) LOGIC (TIMER) 
  When drive powered up, red LED stays on and spindle motor runs
continuously. Check also UA1, UB4, UC2, UC4, UC6, UC7, and UD3. 

UE4 LM311 COMPARITOR (READ) 
  Drive powers up and resets normally. Spindle motor runs, stepper
moves slightly, but "FILE NOT FOUND" error, and red LED flashes.
Check also UF3 and UF4. 

UE6 74LS193 (BINARY COUNTER) 
  Drive powers up and resets normally, but when LOAD is attempted,
screen indicates "SEARCHING FOR ..." red LED does not light and
spindle runs continuously. Check also UD4. 

UF3 NE592N (LM592) READ PREAMP
  Drive powers up and resets normally. Spindle motor runs, stepper
moves slightly, but "FILE NOT FOUND" error and red LED flashes. 
Check also UF4 and UE4. 

UF4 NE592N (LM592) READ AMPLIFIER
  Drive powers up and resets normally. Spindle motor runs, stepper
moves slightly, but "FILE NOT FOUND" error and red LED flashes. 
Check also UF3 and UE4. 

VR1 UA7812KC (LM340KC-12) +12 VOLT REGULATOR
  When powered up, green power LED comes on and red LED comes on and
goes out normally, but motors do not run (or move slowly). Drive 
access will produce a flashing red activity LED and error messages 
"file not found" or "drive not ready" on the error channel. Note 
that a shorted Tantalum capacitor C15 can drop the +12V line! 

VR2 UA7805KC (LM340KC-5.0) +5 VOLT REGULATOR
  Green (power) LED dim, flickers, or does not come on at all. Drive
appears dead, but spindle motor runs continuously. 

CR1  2 AMP 200V BRIDGE RECTIFIER (FOR +5V) 
  Drive appears dead, but spindle motor runs continuously with both 
green and red LEDs dim or dark. May be intermittant and fail after 
warmup. This part normally runs hot.

CR3  2 AMP 200V BRIDGE RECTIFIER (FOR +12V) 
  Drive appears to power up normally, but motors do not run. Should 
get hot only if drive is accessed (motors running) continuously. 

Notes:  UC2, UC3, UB4, and regulators VR1 and VR2 run warm normally
and bridge rectifiers CR1 and CR3 can run very hot if drive is being 
accessed. Otherwise, only CR1 (the 5V source) will get hot.

Newtronics drives (twist type door latch) normally run a bit noiser
(stepper chatter) than earlier ALPS (push down door) types. That 
mechanism also suffers a high failure rate (open) of the R/W head!

Ray Carlsen CET
CARLSEN ELECTRONICS... a leader in trailing-edge technology.
Questions and comments are welcome, especially if you spot a mistake
here. Thanks!
```