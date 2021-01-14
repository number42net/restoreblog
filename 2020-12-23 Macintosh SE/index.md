# Macintosh SE

I purchased this computer in a lot together with a Macintosh II Classic. It was sold as working, but after I turned it on for the first time I found that the hard disk was faulty. 

Overall the condition was decent, the machine was very dirty and yellowed, but technically in very good condition. All the capacitors checked out and aside from the hard disk and the battery no repairs were needed.

Let's see if I can turn this yellow duckling into a beautiful ~~white swan~~ platinum Macintosh.

##### Work done:

* Full inspection and testing
* Deep cleaning inside and out
* Hard disk replacement
* Hard disk indicator LED replacement
* Floppy drive cleaning and libration
* Purposely no re-capping as the capacitors in this model are not prone to failure. Capacitors were inspected and tested instead.
* Colour restoration of the plastic
* Fully reversible external battery modification

##### Todo list:

* Re-installation
* Keyboard and mouse clean up

## Exterior inspection:

This machine was very yellowed and dirty, after a full clean it was already a few tints lighter. 

![Front before cleaning](IMG_20201223_112723.jpg)

In the back I found a 10BASE-2 network card installed (more on this below):

![Back before cleaning](IMG_20201223_112745.jpg)

Plenty of scuff marks all around, luckily I was able to clean all of them off. 

![Left side before cleaning](IMG_20201223_112758.jpg)

![Right side before cleaning](IMG_20201223_112811.jpg)

The bottom was the only part still showing the original colour of the plastic:

![Bottom before cleaning](IMG_20201223_112829.jpg)

## Internal inspection and cleaning:

In these pictures you can see the logic board the way it came out of the machine, with and without the network card installed:

![Logic board and network card](IMG_20201223_114057.jpg)

The memory was already maxed out with 4MB installed, together with a full load of dust:

![Logic board and network card disconnected](IMG_20201223_114202.jpg)

The logic board cleaned up very nice:

![Logic board front - Clean](IMG_20201223_115308.jpg)

No obvious evidence of previous repairs:

![Logic board back - Clean](IMG_20201223_115436.jpg)

This is the Dynaport E/SE 10BASE-2 network adapter. I haven't re-installed this board since it doesn't support 10BASE-T, making it pretty useless in the modern world:

![Network card](IMG_20201223_120708.jpg)

The analogue board fresh out of the case with lots of caked on dust:

![Analogue board before cleaning](IMG_20201223_195446.jpg)

The same board after thorough cleaning: 

![Analogue board after cleaning](IMG_20201223_203112.jpg)

The CRT connector board after cleaning and testing:

![CRT board](IMG_20201223_203735.jpg)

The power supply:

![Power supply closed](IMG_20201223_203909.jpg)

![Power supply open](IMG_20201223_204205.jpg)

## Floppy drive cleaning:

The floppy drive was in quite a state when I took it out, these models lack the dust flap usually found on PCs, and it shows:

![Floppy drive before cleaning](IMG_20201223_155458.jpg)

Fully disassembled:

![Floppy drive disassembled](IMG_20201223_163611.jpg)

Fully cleaned, lubed and ready for re-assembly:

![Floppy drive disassembled cleaned and lubed](IMG_20201223_173632.jpg)

## Hard disk replacement:

Upon first boot I found that the original hard disk's heads were seized. Unfortunately this hard disk could not be saved:

![Old HDD](IMG_20201223_140955.jpg)

I found the following replacement hard disk:

![New HDD front](IMG_20210101_152707.jpg)

![New HDD back](IMG_20210101_152716.jpg)

Using the replacement hard disk it booted into a Dutch System 7.0.1 without any issues: 

![Happy Mac](IMG_20201223_122605.jpg)

## Hard disk activity indicator replacement:

After replacing the hard disk the activity indicator still wouldn't light, I replaced it with a similar style LED with an inline resistor to ensure longevity:

![Drive cage assembled and LED light replaced](IMG_20210101_172857.jpg)

## External battery modification

Although the original battery had not yet started to leak, it was already well below 1v. I replaced it with an externally accessible CR2032 battery. This way it's easy to remove the battery for long term storage and even if it leaks it won't affect the board.

Here is the original battery for reference:

![Original battery](IMG_20210101_173212.jpg)

I soldered new wires directly to the clipped battery leads with an 1N5819 Schottky diode inline. Although this Macintosh should not charge the battery,  it never hurts to add a bit extra safety. 

Before adding heat shrink tube and hot glue for strain relief:

![Battery wiring](IMG_20210101_183803.jpg)

A 3D printed bracket I designed is used to hold a CR2032 battery in the slot left open after the network card was removed:

![3D render of bracket](screenshot1.png)

## Keyboard

The keyboard was a bit yellowed, but most of all it needed a proper deep clean to get years of dirt out of it.

![Keyboard before cleaning](IMG_20210107_150819.jpg)

Here is a picture after fully disassembling and cleaning the keyboard.

![Keyboard disassembled](IMG_20210107_170338.jpg)

Next was removing the yellowing of the plastic, on this particular keyboard both the keys and the case were quite discoloured.

![Before de-yellowing](IMG_20210113_113736.jpg)

![After de-yellowing](IMG_20210113_150426.jpg)

And then the keyboard in all of its clean platinum glory.

![Keyboard done](IMG_20210113_161534.jpg)