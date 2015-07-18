'''
Created on 18.07.2015

@author: gereon
'''

# For handling filesystem paths.
import os.path

##############################################################
# PARAMETERS:
##############################################################


# A list of full paths to directories that are to be searched
# for media.
# Search happens recursively. All media files that are contained
# in a directory the name of which can be interpreted numerically
# are assigned to the button that has this numerical interpretation
# as its index

script_dir = os.path.dirname(os.path.realpath(__file__))

media_dirs = map(os.path.abspath, [os.path.join(script_dir, "resources"), "/media"])
            
# Name suffices of files that are to be recognized as media files
audio_extensions = ".wav", ".mp2", ".mp3"
video_extensions = ".mp4", ".mpeg", ".mov"
media_extensions = audio_extensions + video_extensions

from button import Button

# Maps GPIO pin numbers to button indices
buttons = dict(map(lambda btn : (btn.getIndex(), btn),
          [Button(7, 0),
           Button(11, 1),
           Button(13, 2),
           Button(15, 3),
           Button(31, 4),
           Button(33, 5),
           Button(35, 6),
           Button(37, 7),
           Button(32, 8),
           Button(36, 9),
           Button(38, 10),
           Button(40, 11)]))
