#!/usr/bin/python3

# Copyricht (C) 2015 by the Schwarzenholz Birthday Connection

# The configuration:
from config import *

# Helper functions:
from util import *

# This API gives access to the "General Purpose Input/Output"
# of the Pi board
import RPi.GPIO as GPIO

# For sleeping between button events.
import time

log("Initializing pins for button input...")
 # Make sure that pins are numbered according to the P1 header of the Pi board.
GPIO.setmode(GPIO.BOARD)

# Set our button channels to input mode:
for chn in button_indices.keys():
	print(chn)
	GPIO.setup(chn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
logLine("Done.")



log("Indexing storage media...")

media = {} # A dict mapping button indices (int) to lists of media file paths
for _, bi in button_indices.items():
	media[bi] = []

fc = 0 # The number of files that have been recognized as media files.

# Search for media:
for root in media_dirs:
	for dirpath, _, filenames in os.walk(root):
		
		dirname = os.path.basename(dirpath)

		buttonIndex = None
		try:
			buttonIndex = interpretNumerically(dirname)
		except ValueError:
			continue
		
		for fn in filenames:
			if fn.endswith(media_extensions):
				media[buttonIndex].append(os.path.join(dirpath, fn))
				fc += 1

logLine("Done. {fc} files have been selected.".format(fc=fc))



# Start listening for button events:

def on_edge(channel):
	'''
	Handles voltage edges on the button channels.
	'''
	
	time.sleep(0.05) # Without this sleep, the GPIO.input call apparently alwways returns True
	
	# The assignment of channel value to even type is mysterious to me...
	if GPIO.input(channel):
		on_button_up(button_indices[channel]) 
	else: 
		on_button_down(button_indices[channel])

for chn in button_indices.keys():
	GPIO.add_event_detect(chn, GPIO.BOTH, callback=on_edge, bouncetime=50)


# Play a welcome medium:
playRandomMedium(media[0])

 
def on_button_down(buttonIndex):
	logLine("Button {bi} down!".format(bi=buttonIndex))
	
def on_button_up(buttonIndex):
	logLine("Button {bi} up!".format(bi=buttonIndex))
  
try:  

	while True:
		time.sleep(3600)        # wait 30 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  