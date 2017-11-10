#!/usr/bin/python

# MIDI library
# http://trac.chrisarndt.de/code/wiki/python-rtmidi
import rtmidi
# OSC library
# https://pypi.python.org/pypi/python-osc
from pythonosc import osc_message_builder
import subprocess

device_name = "IAC Driver Bus 1"

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    port_index = available_ports.index(device_name)
    midiout.open_port(port_index)
else:
    midiout.open_virtual_port("My virtual output")

mode = { "ableton mode" : 1,
         "ableton alt mode" : 2,
         "generic mode" : 0
       }

def midi_to_monome(event):
    apc40_y = [53,54,55,56,57,52,51,50,49,48] # MIDI note number
    x = event[1]
    y = apc40_y.index(event[0]) + 1
    state = event[2]
    return [x,y,state]

def monome_to_midi(event):
    # monome protocol
    # https://monome.org/docs/osc/
    return "noteon"

#print midi_to_monome([52,3,0])

def set_mode(m_type):
    if (m_type == 1):
        sysex = [0xF0,0x47,0x00,0x73,0x60,0x00,0x04,0x41,0x01,0x01,0x00,0xF7]
        midiout.send_message(sysex)
    elif (m_type == 2):
        sysex = [0xF0,0x47,0x00,0x73,0x60,0x00,0x04,0x42,0x01,0x01,0x00,0xF7]
        midiout.send_message(sysex)
    else:
        sysex = [0xF0,0x47,0x00,0x73,0x60,0x00,0x04,0x40,0x01,0x01,0x00,0xF7]
        midiout.send_message(sysex)

set_mode(mode["ableton mode"])

# here's the server
# https://github.com/monome/serialosc/blob/master/src/serialosc-device/server.c
