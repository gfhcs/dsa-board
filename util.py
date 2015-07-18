# This file contains helper functions for media-control.py
# Copyricht (C) 2015 by the Schwarzenholz Birthday Connection

# coding=utf8

# For randomness:
import random
random.seed()

# The configuration:
from config import *

# For running shell commands:
from subprocess import *


def log(msg):
	print(msg, end="")

def logLine(msg=""):
	log(msg)
	log('\n')


def interpretNumerically(fileName):
	'''
	Tries to interpret the given file name as a number and
	returns this number. If interpretation fails, a ValueError
	is raised.
	'''
	
	try:
		return int(fileName)
	except:
		raise ValueError("Could not interpret the file name '{fileName}' as a number!".format(fileName=fileName))


def playRandomMedium(mediaPaths):
	'''
	Randomly selects one of the given media paths and plays the designated file.
	The given iterable must contain full paths.
	'''
	try:
		playMedium(random.choice(mediaPaths))
	except IndexError:
		pass


def playMedium(filePath):
	
	playerCommand = 'mpg123'
	
	if os.path.splitext(filePath) in video_extensions:
		playerCommand = 'omxplayer'
	
	args = [playerCommand, filePath]

	log("Command:")
	for arg in args:
		log(" "+ arg)
	
	logLine()

	Popen(args)