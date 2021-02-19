# Retro clock using a Russian IV-18 VFD tube

I've been wanting to build a clock for a few years already, initially using Nixie tubes, but after seeing endless projects based on them I had seen enough.

Then I came across these amazing Russian IV-18 VFD (Vacuum Florescend Display) tubes and decided they would make for a perfect clock.

![Example](img_001.jpg)

## Work done so far: 

+ Initial research
+ Purchasing tubes and driver IC

## Planned work: 

+ Create a working circuit
+ Design the clock

## Initial reseach

Below are some of my research notes on the tube and driver IC, these are likely to change over time.

### IV-18 tube

![IV-18](img_002.jpg)

+ Grid voltage: 20-30v DC should work, but AC might be better.
+ Filament voltage: 3-5v DC
+ Lifespan: Unknown, various sources claim different numbers

### Driver IC

![MAX6921AWI](img_003.jpg)

I've chosen the MAX6921AWI VFD driver IC, mainly because it has sufficient pins to drive all segments and is still reasonably easy to solder. 

### Example circuit

![Circuit](img_004.png)
