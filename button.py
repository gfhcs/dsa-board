'''
Created on 18.07.2015

@author: gereon
'''

# This API gives access to the "General Purpose Input/Output"
# of the Pi board

# Helper functions:
from util import *
from config import *
import RPi.GPIO as GPIO
import random
random.seed()
import time

from subprocess import *

log("Initializing pins for button input...")
# Make sure that pins are numbered according to the P1 header of the Pi board.
GPIO.setmode(GPIO.BOARD)  
logLine("Done.")


class Button(object):
    '''
    Represents a button.
    '''

    def __init__(self, pin, index):
        '''
        Creates a new button instance.
        '''
        self._pin = pin
        self._index = index
        self._process = None
        self._media = []
        self._enabled = False
        
        self._downTime = time.time()
        
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def getEnabled(self):
        return self._endabled
    
    def enable(self):
        if self._enabled:
            return
        GPIO.add_event_detect(self._pin, GPIO.BOTH, callback=self._on_edge, bouncetime=50)
        self._enabled = True
        
    def disable(self):
        if not self._enabled:
            return
        
        self._enabled = False
        GPIO.remove_event_detect(self._pin)

    def getIndex(self):
        return self._index
    
    def getPin(self):
        return self._pin
        
    def assignMedium(self, path):
        self._media.append(path)
        
    def _processActive(self):
        if self._process is None:
            return False
        elif self._process.poll() != 0:
            return True
        else:
            self._process = None
            return False
        
    def play(self, loop=False):
        '''
        Randomly selects one of the assigned media and plays it.
        :param loop: Loops the selected medium indefinetly.
        '''
        
        if self._processActive():
            return
        
        try:
            filePath = random.choice(self._media)
        except IndexError:
            return
        
        playerCommand = 'mpg123'
        loopArg = 'loop -10'
        
        if filePath.endswith(video_extensions):
            playerCommand = 'omxplayer'
            loopArg = '--loop'
        
        args = [playerCommand]
        
        if loop:
            args.append(loopArg)
    
        args.append(filePath)
    
        log("Command:")
        for arg in args:
            log(" "+ arg)
        
        logLine()

        self._process = Popen(args)
        
    def abort(self):
        if not self._processActive():
            return
        
        log("Killing process...")
        self._process.kill()
        self._process = None
        logLine("Done.")
             
    def _on_edge(self, channel):
        '''
        Handles voltage edges on the button channels.
        '''
        
        time.sleep(0.05) # Without this sleep, the GPIO.input call apparently alwways returns True
        
        # The assignment of channel value to even type is mysterious to me...
        if GPIO.input(channel):
            self.on_up()
        else: 
            self.on_down()

    def on_down(self):
        logLine("Button {bi} down!".format(bi=self._index))
        self._downTime = time.time()
        
    def on_up(self):
        logLine("Button {bi} up!".format(bi=self._index))
        
        logLine(time.time() - self._downTime)
        
        if self._processActive():
            self.abort()
        else:
            self.play(time.time() - self._downTime >= 3)
            

