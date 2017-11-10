#!/usr/bin/python

# MIDI library
# http://trac.chrisarndt.de/code/wiki/python-rtmidi
import rtmidi
# OSC library
# https://pypi.python.org/pypi/python-osc
from pythonosc import osc_message_builder
from pythonosc import dispatcher
from pythonosc import osc_server

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

apc40_y = [53,54,55,56,57,52,51,50,49,48] # MIDI note numbers in order, top to bottom, each row

def midi_to_monome(event):
    # this is the MIDI input callback
    # http://www.music.mcgill.ca/~gary/rtmidi/index.html#input
    x = event[1]
    y = apc40_y.index(event[0]) + 1
    state = event[2]
    return ["/monome/grid/key",x,y,state]

def monome_to_midi(event):
    # monome protocol
    # https://monome.org/docs/osc/
    # "/monome/grid/led/set %s %s %s" % (x,y,state)
    parts = event.split(' ')
    if (parts[0] == "/monome/grid/led/set"):
        print("set one led")
    elif (parts[0] == "/monome/grid/led/all"):
        print("set all leds")
    elif (parts[0] == "/monome/grid/led/map"):
        print("set some leds")
    elif (parts[0] == "/monome/grid/led/row"):
        print("set a row of leds")
    elif (parts[0] == "/monome/grid/led/col"):
        print("set a column of leds")
    else:
        print("unknown message %s" % event)

    if (parts[3]):
        midi = [0x90, parts[2], apc40_y.index(parts[1]), 127]
        print("LED on, 0x90")
    else:
        midi = [0x80, parts[2], apc40_y.index(parts[1]), parts[3]]
        print("LED off 0x80")

    return midi

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

# TODO where do we start a rtmidi callback loop? Is this a multithreaded
# application?
if __name__ == "__main__":
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/monome/grid", print)

    server = osc_server.ThreadingOSCUDPServer(
      ("127.0.0.1", 8000), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
