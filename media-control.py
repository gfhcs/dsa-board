#!/usr/bin/python3

# Copyricht (C) 2015 by the Schwarzenholz Birthday Connection

# The configuration:
from config import *

# Helper functions:
from util import *


# For sleeping between button events.
import time

log("Indexing storage media...")

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
				try:
					buttons[buttonIndex].assignMedium(os.path.join(dirpath, fn))
					fc += 1
				except KeyError:
					pass

logLine("Done. {fc} files have been selected.".format(fc=fc))

# Start listening for button events:

time.sleep(3) # Delay until Pi's audio system is up.

# Play a welcome medium:
buttons[0].play()

for btn in buttons.values():
	btn.enable()
  
try:  

	while True:
		time.sleep(3600)        # wait 30 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  