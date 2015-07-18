# This file contains helper functions for media-control.py
# Copyricht (C) 2015 by the Schwarzenholz Birthday Connection

# coding=utf8


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


	