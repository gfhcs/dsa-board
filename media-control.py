#!/usr/bin/python3

# Copyricht (C) 2015 by the Schwarzenholz Birthday Connection


# For handling filesystem paths.
import os.path
# Helper functions:
from util import *


##############################################################
# PARAMETERS:
##############################################################

# Maps GPIO pin numbers to button indices
# TODO: Fill in proper button channels here!
button_indices = {1 : 0,
				  2 : 1,
				  3 : 2}

# A list of full paths to directories that are to be searched
# for media.
# Search happens recursively. All media files that are contained
# in a directory the name of which can be interpreted numerically
# are assigned to the button that has this numerical interpretation
# as its index
media_dirs = map(os.path.abspath, ["resources"])
            
# Name suffices of files that are to be recognized as media files
extensions = ".wav", ".mp2", ".mp3", ".mp4", ".mpeg"

##############################################################


# This API gives access to the "General Purpose Input/Output"
# of the Pi board
import RPi.GPIO as GPIO



log("Initializing pins for button input...")
 # Make sure that pins are numbered according to the P1 header of the Pi board.
GPIO.setmode(GPIO.BOARD)

# Set our button channels to input mode:
for chn in button_channels:
	GPIO.setup(ch, GPIO.IN)
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
			if fn.endswith(extensions):
				media[buttonIndex].append(os.path.join(dirpath, fn))
				fc += 1

logLine("Done. {fc} files have been selected.".format(fc=fc))


# Everything is set up.
# Wait for button presses and play files:

# Start listening for button events:
GPIO.add_event_detect(25, GPIO.RISING, callback=lambda channel : on_button_down(button_indices[channel]))
GPIO.add_event_detect(25, GPIO.FALLING, callback=lambda channel : on_button_up(button_indices[channel]))

# Play a welcome medium:
playRandomMedium(media[0])

 
def on_button_down(buttonIndex):
	logLine("Button {bi} down!".format(bi=buttonIndex))
	
def on_button_up(buttonIndex):
	logLine("Button {bi} up!".format(bi=buttonIndex))
  
try:  

    sleep(float('inf'))         # wait 30 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  