# XBee3 MicroPython APA102

This project has instructions and code for wiring up an APA102 LED strip or panel
with an XBee3 device with MicroPython. The images in this project are of a Digi XBee Cellular LTE Cat 1 Verizon development kit (XKC-V1T-U), but this code should work
with any MicroPython device.  

This implementation assumes an XBee3 device that does not have SPI support in
Micropython so it contains a pure MicroPython implementation of the APA102 driver 
and SPI using whichever digital outputs you choose. Because of the pure MicroPython
implementation of SPI it's very slow and can take multiple seconds to update all
of the LEDs (and hence it is more of an experiment than a practical library).

##### Wiring
1. Connect the 5V pin of the APA102 to some +5V power source (I used a USB cord)
2. Connect the GND pin of the APA102 to the GND pin of the XBee3 device and the GND of
3. Also connect the GND pin of the APA102 to the GND wire of your +5V power source
4. Connect the DI pin of the APA102 to the DIO4 (pin 11) pin of the XBee3 device
5. Connect the CI pin of the FeatherWing to the DIO2 (pin 18) pin of the XBee3 device

![xbee_to_apa102](https://github.com/cpopp/XBee3-MicroPython-APA102/raw/master/images/apa102back.jpg)
In this image you'll the black wire of the APA102 (5V) goes to the +5V wire from a severed USB cable.  The blue wire of the APA102 (GND) goes to the GND wire of the severed USB cable and also to the GND pin of the XBee3 device.  The green wire of the APA102 (DI) goes to DIO4 (pin 11) of th XBee device.  The red wire of the APA102 (CI) goes to DIO2 (pin 18) of the XBee3 device.

##### Dependencies
The code is entirely standalone with no dependencies.

##### Application code
The code in apa102.py sets up DIO2 and DIO4 as digital output
pins that will be used to send the SPI signals to the APA102.  If you prefer to use
different pins you can adjust the constants SPI_CLK_PIN and SPI_MOSI_PIN.

You will need to adjust the constant LED_COUNT with the nuber of LEDs in your
APA102 strip or panel.  

To run this code you can use the flash compile mode on the XBee.  Copy the code in
xbee_ina219.py and then hit Ctrl-F in a MicroPython interpreter terminal.  Paste the
code and hit Ctrl-D.  Enter N to skip running the code automatically.  You can now
hit Ctrl-R to run the code and get a power reading.

At this point you are ready to hook up a load to measure.

##### Working examples
![apa102_panel](https://github.com/cpopp/XBee3-MicroPython-APA102/raw/master/images/apa102front.jpg)

![apa102_strip](https://raw.githubusercontent.com/cpopp/XBee3-MicroPython-APA102/master/images/apa102strip.jpg)

##### Tweaks for longer LED strips
The code currently sends one end frame regardless of the number of LEDs.  I don't
have an LED strip with more than 64 LEDs to try, but you will likely need
to send an additional end frame for each additional 64 LEDs you use.

##### SK9822 LEDs
The SK9822 LEDs are a clone of the APA102 that use nearly the same protocol.
I don't have any of these to test with but I believe it should work by just
sending an extra end frame.

##### References
Guide to APA102 with micro:bit: http://www.smythe-consulting.com/2017/03/driving-dotstar-apa102-led-strings-with.html

Digi MicroPython Programming Guide: https://www.digi.com/resources/documentation/digidocs/90002219

SK9822 and APA102 comparison: https://cpldcpu.wordpress.com/2016/12/13/sk9822-a-clone-of-the-apa102/
