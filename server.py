#!/usr/bin/python

# MIDI library
# https://github.com/SpotlightKid/python-rtmidi
import rtmidi
from rtmidi.midiconstants import NOTE_OFF, NOTE_ON
# OSC library
# https://github.com/attwad/python-osc
from pythonosc import osc_message_builder
from pythonosc import dispatcher
from pythonosc import osc_server

#device_name = "IAC Driver Bus 1"
device_name = 'Akai APC40:Akai APC40 MIDI 1 16:0'

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

apc40_x = 8 # size
apc40_y = [53,54,55,56,57,52,51,50,49,48] # MIDI note numbers in order, top to bottom, each row

def makenote(x, y, state):
    if (state):
        midi = [NOTE_ON | (x - 1), apc40_y[y - 1], state]
        midiout.send_message(midi)
    else:
        midi = [NOTE_OFF | (x - 1), apc40_y[y - 1], state]
        midiout.send_message(midi)

def monome_grid_led_set(namespace, x, y, state):
    # monome protocol
    # https://monome.org/docs/osc/
    makenote(x, y, state)
    print("%s %s %s %s" % (namespace, x, y, state)) 

def monome_grid_led_all(namespace, state):
    # outer loop for x, inner loop for y
    for x in range(apc40_x):
        for y in range(len(apc40_y)):
            print("%s %s %s %s" % (namespace, x + 1, y + 1, state)) 
            makenote(x + 1, y + 1, state)

def monome_grid_led_map(namespace, x, y, bitmask, state):
    print("set some leds")

def monome_grid_led_row(namespace, x_offset, y, state):
    for x in range(apc40_x):
        print("%s %s %s %s" % (namespace, x + 1, y, state)) 
        makenote(x + 1, y, state)

def monome_grid_led_col(namespace, x, y_offset, state):
    for y in range(len(apc40_y)):
        print("%s %s %s %s" % (namespace, x, y + 1, state)) 
        makenote(x, y + 1, state)

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

# here's the official Monome server
# https://github.com/monome/serialosc/blob/master/src/serialosc-device/server.c

if __name__ == "__main__":
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/monome/grid/led/set", monome_grid_led_set)
    dispatcher.map("/monome/grid/led/all", monome_grid_led_all)
    dispatcher.map("/monome/grid/led/map", monome_grid_led_map)
    dispatcher.map("/monome/grid/led/row", monome_grid_led_row)
    dispatcher.map("/monome/grid/led/col", monome_grid_led_col)
    dispatcher.map("/monome/grid/key", print)

    server = osc_server.ThreadingOSCUDPServer(
      ("127.0.0.1", 8000), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
