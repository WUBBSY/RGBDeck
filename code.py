# Steam Deck NeoPixel Rainbow Swirl

import board
import adafruit_dotstar as dotstar
import time
import neopixel

# One pixel connected internally!
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

# NeoPixel strip (of 15 LEDs) connected on D4
NUMPIXELS = 15 # Change this value if you use more or less than 15 LEDs
neopixels = neopixel.NeoPixel(board.D4, NUMPIXELS, brightness=0.2, auto_write=False)

######################### HELPERS ##############################

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return (0, 0, 0)
    if (pos > 255):
        return (0, 0, 0)
    if (pos < 85):
        return (int(pos * 3), int(255 - (pos*3)), 0)
    elif (pos < 170):
        pos -= 85
        return (int(255 - pos*3), 0, int(pos*3))
    else:
        pos -= 170
        return (0, int(pos*3), int(255 - pos*3))

######################### MAIN LOOP ##############################

i = 0
while True:
  # spin internal LED around! autoshow is on
  dot[0] = wheel(i & 255)

  # also make the neopixels swirl around
  for p in range(NUMPIXELS):
      idx = int ((p * 256 / NUMPIXELS) + i)
      neopixels[p] = wheel(idx & 255)
  neopixels.show()

  i = (i+1) % 256  # run from 0 to 255
  #time.sleep(0.01) # make bigger to slow down