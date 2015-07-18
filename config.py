'''
Created on 18.07.2015

@author: gereon
'''

# For handling filesystem paths.
import os.path


##############################################################
# PARAMETERS:
##############################################################

# Maps GPIO pin numbers to button indices
# TODO: Fill in proper button channels here!
button_indices = {7 : 0,
                  11 : 1,
                  13 : 2}

# A list of full paths to directories that are to be searched
# for media.
# Search happens recursively. All media files that are contained
# in a directory the name of which can be interpreted numerically
# are assigned to the button that has this numerical interpretation
# as its index
media_dirs = map(os.path.abspath, ["resources"])
            
# Name suffices of files that are to be recognized as media files
audio_extensions = ".wav", ".mp2", ".mp3"
video_extensions = ".mp4", ".mpeg", ".mov"
media_extensions = audio_extensions + video_extensions

##############################################################
