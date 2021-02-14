# Commodore 64 bread bin

As usual, I purchased this Commodore 64 locally untested, the computer itself was working perfectly, but the 1541 floppy drive needed some work. 

![Cleaned up](IMG_20210214_193656.jpg)

## Work done so far: 

+ Initial inspection and testing
+ Clean up
+ 1571 floppy drive repair
+ Case repair

## Planned work: 

+ Full testing using test ROM
+ Power cable repair
+ Power adapter proactive maintenance
+ JiffyDOS conversion

## Exterior inspection:

Like most computers coming across my bench, this Commodore had seen better days. Maybe one day it was a treasured home computer, right now it was a filthy mess.

![Top](IMG_20210214_095228.jpg)

![Bottom](IMG_20210214_095249.jpg)

![Left](IMG_20210214_095310.jpg)

![Back](IMG_20210214_095325.jpg)

The power connector in particular had seen better days:

![Rusty power](IMG_20210214_095826.jpg)

The power supply itself has a date code stamped onto it: 10 October 1984, which matches the date codes on the chips pretty well.

![Date stamp](IMG_20210214_110015.jpg)

![Back power supply](IMG_20210214_110031.jpg)

One unfortunate problem is that all but 1 of the plastic hinges in the back of the case had already been snapped off by a previous owner and the last one came off when I opened the case my self. More on this below.

## Board inspection:

I had already spotted that the RF shield was still in place from the outside:

![Shield](IMG_20210214_110511.jpg)

The board itself was in better shape than I had expected from the look of the power cable:

![Board top](IMG_20210214_110800.jpg)

On the bottom we can see that the solder joints have been reworked at some point. Either really messy work from the factory, or more likely a repair later in its life:

![Board bottom](IMG_20210214_110843.jpg)

![Rework](IMG_20210214_110851.jpg)

I decided to do a quick clean up and remove all the flux residue:

![Clean-up bottom](IMG_20210214_130517.jpg)

## First boot

After this it was time to check the voltages on the power supply, which all checked out (9v AC and 5v DC), time for a test:

![First boot](IMG_20210214_112037.jpg)

IT WORKS!

## Keyboard clean up:

The keyboard was particularly dirty, and I ended up taking it fully apart to do a thorough clean up:

![Keyboard dirty](IMG_20210214_132729.jpg)

![Keyboard dirtier](IMG_20210214_142220.jpg)

![Clean PCB](IMG_20210214_143101.jpg)

![Clean keyboard case](IMG_20210214_145026.jpg)

## 1541 floppy drive

The 1541 is a special beast, it's not just a floppy drive, but a full 8-bit computer in its own right, with a MOS 6502 CPU, RAM, ROM and related logic chips.

![Floppy drive top](IMG_20210214_151123.jpg)

![Floppy drive front](IMG_20210214_151232.jpg)

![Floppy drive back](IMG_20210214_151301.jpg)

After opening up the drive and doing a quick inspection of the belt and general condition I tried powering it on: The motor started spinning straight away, but unfortunately didn't stop spinning as it should. Instead, I was greeted by 3 slow red flashes followed by a pause, which continued indefinitely. 

I started off probing the voltages, which all checked out and then moved on to the oscilloscope. On the CPU side everything seemed fine, data and address lines were active. 

Thanks to the great work of [Ray Carlson](http://personalpages.tds.net/~rcarlsen/cbm/1541/1541chip.txt) I was quickly pointed into the direction of the ROMs. The ROM in location UB4 seemed perfectly fine, but UB3 had badly corroded pins. 

![Corroded pins](IMG_20210214_154530.jpg)

After a quick clean up the issue was fully resolved, which meant moving on to the mechanical side. After freeing and lubricating the shafts on which the heads moved it was time for testing. 

I connected everything up and played a quick round of Landing on TB19 with my son!

![Playing a game](IMG_20210214_200930.jpg)

## Case repair

As mentioned above, when I opened the case I managed to break off the last remaining hinge on the back of the case. Luckily there are great 3D designs ![available](https://www.thingiverse.com/thing:3092874), I printed a set and glued them in place:

![New hinge front](IMG_20210214_171244.jpg)

![New hinge back](IMG_20210214_172015.jpg)