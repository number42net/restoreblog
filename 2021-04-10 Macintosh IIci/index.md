# Macintosh II/ci
This computer belongs to a customer who requested a full recap and floppy drive refurbishment.

#### Work done so far
+ Replace capacitors from main board and power supply
+ Clean main board and power supply
+ Clean and lubricate floppy drive
+ Failed repair attempt of the floppy drive

#### Planned work
+ Full diagnostic run for several hours of burn in

# Initial inspection
Here is the case opened up and the board removed:

![Case opened up](img_001.jpg)

![Board removed](img_002.jpg)

There was already quite a mess from the leaking electrolytic capacitors:

![Electrolytic mess](img_003.jpg)

![Electrolytic mess](img_004.jpg)

# Main board
After removing the old capacitors I gave the board a thorough cleaning:

![Fully cleaned](img_009.jpg)

A few suspect traces were found, these will be cleaned, tinned and protected with new solder mask.

![Bad traces](img_005.jpg)

![Bad traces](img_006.jpg)

![Bad traces](img_007.jpg)

![Bad traces](img_008.jpg)

And here is the finished result, the old electrolytic capacitors have been replaced with tantalum versions, bad traces have been repaired, the whole board has been thoroughly cleaned and a new battery fitted:

![Logic board completed](img_021.jpg)

Here is the machine powered:

![Memory](img_016.jpg)


# Power supply
Once the motherboard was done, it was time to move on to the power supply. 

![PSU opened up](img_010.jpg)

![PSU opened up](img_011.jpg)

Overall it was cleaner than I had expected, but the fan was pretty crusty:

![Dirty fan](img_012.jpg)

After cleaning, I found it spun freely, so no need to replace it:

![Clean fan](img_013.jpg)

Here are all the capacitors removed:

![Power supply removed](img_014.jpg)

And the following are pictures of the power supply being re-assembled with the new capacitors, aside from the electrolytics I also replaced 4 Rifa capacitors which can cause a lot of problems:

![PSU main board](img_023.jpg)

![PSU main board 2](img_024.jpg)

![PSU case board](img_022.jpg)

![PSU case ready](img_025.jpg)

# Floppy drive
The floppy drive was particularly bad, there was a huge amount of caked on dirt inside:

![Dirty floppy drive](img_017.jpg)

![Very dirty head](img_018.jpg)

Here is the drive fully disassembled:

![Floppy drive disassembled](img_019.jpg)

And the same parts cleaned:

![Cleaned parts](img_020.jpg)

Here it is reassembled, but unfortunately I found more problems while testing. Whenever a floppy is inserted, it is ejected straight away again. 

![Floppy reassembled](img_026.jpg)

I ended up testing with a head assembly from another drive, which worked perfectly. After this I measured the resistance between the pins on each of the header cables. I found that on a known good head assembly all the pins had a small amount of resistance between them, while the bad heads tested open circuit on several pins.

![Floppy drive issues](img_027.jpg)