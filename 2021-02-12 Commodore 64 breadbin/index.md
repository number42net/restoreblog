# Commodore 64 bread bin - Assy 250425

As usual, I purchased this Commodore 64 locally untested, the computer itself was working perfectly, but the 1541 floppy drive needed some work. 

![Cleaned up](img_001.jpg)

## Work done so far: 

+ Initial inspection and testing
+ Clean up
+ 1571 floppy drive repair
+ Case repair
+ Power adapter proactive maintenance

## Planned work: 

+ Full testing using test ROM
+ Power cable repair
+ JiffyDOS conversion?

## Exterior inspection:

Like many computers coming across my bench, this Commodore had seen better days. Maybe one day it was a treasured home computer, right now it was a filthy mess.

![Top](img_002.jpg)

![Bottom](img_003.jpg)

![Left](img_004.jpg)

![Back](img_005.jpg)

The power connector in particular had seen better days:

![Rusty power](img_006.jpg)

The power supply itself has a date code stamped onto it: 10 October 1984, which matches the date codes on the chips pretty well.

![Date stamp](img_007.jpg)

![Back power supply](img_008.jpg)

One unfortunate problem is that all but 1 of the plastic hinges in the back of the case had already been snapped off by a previous owner and the last one came off when I opened the case my self. More on this below.

## Board inspection:

I had already spotted that the RF shield was still in place from the outside:

![Shield](img_009.jpg)

The board itself was in better shape than I had expected from the look of the power cable:

![Board top](img_010.jpg)

On the bottom we can see that the solder joints have been reworked at some point. Either really messy work from the factory, or more likely a repair later in its life:

![Board bottom](img_011.jpg)

![Rework](img_012.jpg)

I decided to do a quick clean up and remove all the flux residue:

![Clean-up bottom](img_013.jpg)

## First boot

After this it was time to check the voltages on the power supply, which all checked out (9v AC and 5v DC), time for a test:

![First boot](img_014.jpg)

IT WORKS!

## Keyboard clean up:

The keyboard was particularly dirty, and I ended up taking it fully apart to do a thorough clean up:

![Keyboard dirty](img_015.jpg)

![Keyboard dirtier](img_016.jpg)

![Clean PCB](img_017.jpg)

![Clean keyboard case](img_018.jpg)

## 1541 floppy drive

The 1541 is a special beast, it's not just a floppy drive, but a full 8-bit computer in its own right, with a MOS 6502 CPU, RAM, ROM and related logic chips.

![Floppy drive top](img_019.jpg)

![Floppy drive front](img_020.jpg)

![Floppy drive back](img_021.jpg)

After opening up the drive and doing a quick inspection of the belt and general condition I tried powering it on: The motor started spinning straight away, but unfortunately didn't stop spinning as it should. Instead, I was greeted by 3 slow red flashes followed by a pause, which continued indefinitely. 

I started off probing the voltages, which all checked out and then moved on to the oscilloscope. On the CPU side everything seemed fine, data and address lines were active. 

Thanks to the great work of [Ray Carlson](http://personalpages.tds.net/~rcarlsen/cbm/1541/1541chip.txt) I was quickly pointed into the direction of the ROMs. The ROM in location UB4 seemed perfectly fine, but UB3 had badly corroded pins. 

![Corroded pins](img_022.jpg)

After a quick clean up the issue was fully resolved, which meant moving on to the mechanical side. After freeing and lubricating the shafts on which the heads moved it was time for testing. 

I connected everything up and played a quick round of Landing on TB19 with my son!

![Playing a game](img_023.jpg)

## Case repair

As mentioned above, when I opened the case I managed to break off the last remaining hinge on the back of the case. Luckily there are great 3D designs [available](https://www.thingiverse.com/thing:3092874), I printed a set and glued them in place:

![New hinge front](img_024.jpg)

![New hinge back](img_025.jpg)

## Power supply refurbishment

The Commodore 64 has a major "Achilles' heel", the power supply. It's build into a separate plastic brick and holds a transformer which sends 9v AC directly to the computer and a small board which contains the rectifier, voltage regulator and related components for the 5v DC supply. The whole brick is filled with potting compound from the factory.

It's this voltage regulator, embedded inside the potted brick which creates the main issue. Over time, they tend  to drift higher, putting more strain on the ICs inside the computer. Eventually they often short, sending the full voltage from the transformer straight to all the sensitive components on the main board, which usually results in many parts failing instantly. 

Here is the back of the original board:

![Back of PCB](img_026.jpg)

Luckily we now have modern replacements for these parts which contain safeties to prevent this type of failure in the first place and also generate barely any heat, compared to the original part which gets really hot.

![Replaced parts](img_027.jpg)

Here I used a Traco Power TSR 2-2450, purchased directly from a certified distributor. It can supply 2A, slightly more than the original 1.5A regulator, which helps to run more demanding cartridges. While I had it open, I also replaced the capacitor with a matching axial model. 

![Power supply back together](img_28.jpg)