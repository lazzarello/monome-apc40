#!/usr/bin/python

# MIDI library
# https://github.com/vishnubob/python-midi
import midi
import midi.sequencer as sequencer
# OSC library
# https://pypi.python.org/pypi/python-osc
from pythonosc import osc_message_builder
import subprocess

client = "16"
port = "0"

mode = { "ableton mode" : 1,
         "ableton alt mode" : 2,
         "generic mode" : 0
       }

# initialize the an ALSA sequencer object
hardware = sequencer.SequencerHardware()

if not client.isdigit:
    client = hardware.get_client(client)

if not port.isdigit:
    port = hardware.get_port(port)

'''
class ReadLoop:
    seq = sequencer.SequencerRead(sequencer_resolution=120)
    seq.subscribe_port(0, 0)
    seq.start_sequencer()
    #while True:
    event = seq.event_read()
    if event is not None:
        print event

class WriteLoop:
    seq = sequencer.SequencerWrite(sequencer_resolution=120)
    seq.subscribe_port(client, port)
    seq.start_sequencer()
    #for event in events:
    #    buf = seq.event_write(event, False, False, True)
    #    if buf == None:
    #        continue
    #    if buf < 1000:
    #        time.sleep(.5)
    #while event.tick > seq.queue_get_tick_time():
    #    seq.drain()
    #    time.sleep(.5)
'''

def midi_to_monome(event):
    apc40_y = [53,54,55,56,57,52,51,50,49,48] # MIDI note number
    x = event[1]
    y = apc40_y.index(event[0]) + 1
    state = event[2]
    return [x,y,state]

#print midi_to_monome([52,3,0])

def set_mode(m_type):
    if (m_type == 1):
        #seq = sequencer.SequencerWrite(sequencer_resolution=120)
        #seq.subscribe_port(client, port)
        #seq.start_sequencer()
        #sysex = midi.SysexEvent(data=[0x47,0x00,0x73,0x60,0x00,0x04,0x40,0x01,0x01,0x00])
        #seq.event_write(sysex, False, False, True)
        sysex = "F0 47 00 73 60 00 04 41 01 01 00 F7"
        subprocess.call(["amidi", "-p", "hw:0,0,0", "-S",sysex])
    if (m_type == 2):
        sysex = [0xF0,0x47,0x00,0x73,0x60,0x00,0x04,0x42,0x01,0x01,0x00,0xF7]
        midi.SysexEvent(data=sysex)
    else:
        sysex = [0xF0,0x47,0x00,0x73,0x60,0x00,0x04,0x40,0x01,0x01,0x00,0xF7]
        midi.SysexEvent(data=sysex)

set_mode(mode["ableton mode"])

# initialize monome
# https://monome.org/docs/osc/
# here's the server
# https://github.com/monome/serialosc/blob/master/src/serialosc-device/server.c
monome = []
