# RGBDeck
RGB Lighting for the Valve Steam Deck

This Project uses a small microcontroller (**Adafruit Trinket M0**) and some **WS2812B** LEDs (aka. NeoPixels or ARGB) to add RGB lighting to the back of the Steam Deck. Best effect when using a translucent back.  

![Front](https://user-images.githubusercontent.com/38454270/216425124-1bf0d9cd-a282-4135-b74b-2863e37c24a7.jpg)

>## Disclaimer:  
> **This Project includes modification of the Steam Deck hardware and soldering of thin wires and small pads. Please be careful as to not damage your hardware.**  
This Mod is finicky and should only be done if you're competent in soldering and working with electronics.  
The Steam Deck contains a Lithium-Polymer battery cell which can be very dangerous if handled improbable.  
**I don't take any responsibility or liability for any damages to you, your hardware or anything else.**  
This mod may also interfere with your WiFi or Bluetooth. I haven't encountered any problems so far, but your mileage may vary. 

## Table of contents
- [RGBDeck](#rgbdeck)
  - [Table of contents](#table-of-contents)
  - [What is needed](#what-is-needed)
  - [Preparing your microcontroller](#prepairing-your-microcontroller)
  - [Connecting the Microcontroller to your Steam Deck](#connecting-the-microcontroller-to-your-steam-deck)
  - [Adding the addressable LEDs](#adding-the-addressable-leds)


## What is needed

- A suitable microcontroller. (This example uses a Adafruit Trinket M0 mainly for it's size)
- WS2812B LEDs (aka. NeoPixels or ARGB). A LED Strip is suitable since in can be mounted easily. 
- thin wire best would be enamelled wire
- Tools to open the Steam Deck (Philips Driver size 0 and a plastic spudger)
- Soldering iron. Preferibly with a small tip since the pads are very small

## Preparing your microcontroller
For this example I'm using an [Adafruit Trinket M0](https://www.adafruit.com/product/3500) which is a very small and low cost microcontroller.  
I'm also using CircuitPython for the program for ease of use. (I might add a Arduino example in the future)

The Adafruit Trinket M0 comes preinstalled with CircuitPython but it is recommended to update it. Adafruit has a simple [guide](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/circuitpython) on how to update/install CircuitPython.  
Additionally you'll need few libraries which can be downloaded from [circuitpython.org](https://circuitpython.org/libraries) (adafruit-circuitpython-bundle-7.x-mpy...)  
After downloading the zip find these files inside the _lib_ folder:  
- adafruit_dotstar.mpy
- adafruit_pixelbuf.mpy
- neopixel.mpy

Copy these Files onto your micro into the _lib_ folder.  
Then Download the _code.py_ and place it in the root directory of your micro. That's it.  
(If you use more or less than 15 LEDs you should change the LED count in the code at line 12)

## Connecting the Microcontroller to your Steam Deck

We fist must remove the back cover of the Steam Deck. A handy guide can be found on [iFixit](https://www.ifixit.com/Guide/Steam+Deck+Back+Cover+Replacement/148893)  
It is then advisable to disconnect the battery to minimize the risk of damage to the components. (Small [guide](https://www.ifixit.com/Guide/Steam+Deck+Battery+Replacement/149070) follow till step 7)  

You now must solder 2 small leads to the left controller board. It's the one on the right with the large "L" and the buttons for the back buttons.  
The negative connection is relatively simple since we can solder it onto the left pad of the lower button which is connected to the ground plane.  
The positive connection is tricky. There is a small test pad a bit left and up from the lower button. This test pad is connected to the 5V rail of the controller. Carefully solder a thin wire to the pad.  
After that you should fixate them with tape or glue them down.  

![BoardView](https://user-images.githubusercontent.com/38454270/216419156-7a13e743-17e9-434c-b82c-dee827b108b5.png)

Now just solder the two cables onto your micro and it should be powered by the Steam Deck.  
![TrinketTop](https://user-images.githubusercontent.com/38454270/216419480-20282663-8417-4ced-b88d-65feef562de0.png)
_Din_ is where you connect your LEDs.  
The large white connector is just for testing purposes and is not needed. 

## Adding the addressable LEDs
NeoPixels or ARGB LEDs contain a WS2812B chip which enables them to be individually controlled.  
These LEDs have 4 contacts _+5V_, _Din_, _Dout_, _GND_.  
_+5V_ and _GND_ are your power connections and need to be connected to the _Gnd_ and _Bat_ or _5V_ connections on your micro.  
_Din_ gets connected to Pin 4 or _D4_ on your micro.  
_Dout_ is the output of the last LED in array and you can connect more LEDs with _Din_ onto it.  

After connecting all your LEDs, you mount them in the back half of your Steam Deck.  
You can follow my setup or experiment with your own placement.  
![BackView](https://user-images.githubusercontent.com/38454270/216421677-a8ab8128-7ac4-4c42-a9e7-88c4b2e85afa.jpg)

**Be careful when attaching the LEDs to the Steam Deck to not short out any connections of the pcbs or the LEDs!**  

After that put back the case, careful to use the correct screws and you're done!
