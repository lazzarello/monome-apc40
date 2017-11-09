#!/usr/bin/python

# MIDI library
# https://github.com/vishnubob/python-midi
import midi
# OSC library
# https://pypi.python.org/pypi/python-osc
from pythonosc import osc_message_builder
# https://github.com/monome/libmonome
# https://monome.org/docs/grid-studies/python/
import monome

# In Mode 1 or Mode 2, all buttons act as momentary buttons.

# initialize values for APC matrix to all off
led_states = { "off" : 0,
               "green" : 1,
               "green blink" : 2,
               "red" : 3,
               "red blink" : 4,
               "yellow" : 5,
               "yellow blink" : 6
              }
apc40 = [
         [1,1]: [53,1,led_states['off']],
         [1,2]: [54,1,led_states['off']],
         [1,3]: [55,1,led_states['off']],
         [1,4]: [56,1,led_states['off']],
         [1,5]: [57,1,led_states['off']],
         [2,1]: [53,2,led_states['off']],
         [2,2]: [54,2,led_states['off']],
         [2,3]: [55,2,led_states['off']],
         [2,4]: [56,2,led_states['off']],
         [2,5]: [57,2,led_states['off']],
         [3,1]: [53,3,led_states['off']],
         [3,2]: [54,3,led_states['off']],
         [3,3]: [56,3,led_states['off']],
         [3,4]: [56,3,led_states['off']],
         [3,5]: [57,3,led_states['off']],
         [4,1]: [53,4,led_states['off']],
         [4,2]: [54,4,led_states['off']],
         [4,3]: [55,4,led_states['off']],
         [4,4]: [56,4,led_states['off']],
         [4,5]: [57,4,led_states['off']],
         [5,1]: [53,5,led_states['off']],
         [5,2]: [54,5,led_states['off']],
         [5,3]: [55,5,led_states['off']],
         [5,4]: [56,5,led_states['off']],
         [5,5]: [57,5,led_states['off']]
        ]
# initialize monome
# https://monome.org/docs/osc/
# here's the server
# https://github.com/monome/serialosc/blob/master/src/serialosc-device/server.c
monome = []
