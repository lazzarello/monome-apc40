#!/usr/bin/python

# MIDI library
# https://github.com/vishnubob/python-midi
import midi
# OSC library
# https://pypi.python.org/pypi/python-osc
from pythonosc import osc_message_builder
# https://github.com/monome/libmonome
# https://monome.org/docs/grid-studies/python/
#import monome

apc40_x = [1,2,3,4,5,6,7,8] # MIDI Channel
apc40_y = [53,54,55,56,57,52,51,50] # MIDI note number

def set_mode(m_type):
    if (m_type == 1):
        sysex = "F0 47 00 73 60 00 04 41 01 01 00 F7"
    if (m_type == 2):
        sysex = "F0 47 00 73 60 00 04 42 01 01 00 F7"
    else:
        sysex = "F0 47 00 73 60 00 04 40 01 01 00 F7"

def midi_to_monome(event):
    x = event[1]
    y = apc40_y.index(event[0]) + 1
    state = event[2]
    return [x,y,state]

print midi_to_monome([52,3,0])

# initialize monome
# https://monome.org/docs/osc/
# here's the server
# https://github.com/monome/serialosc/blob/master/src/serialosc-device/server.c
monome = []
