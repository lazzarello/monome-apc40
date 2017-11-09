#!/usr/bin/python

# MIDI library
# https://github.com/vishnubob/python-midi
import midi.sequencer as sequencer
# OSC library
# https://pypi.python.org/pypi/python-osc
from pythonosc import osc_message_builder
# https://github.com/monome/libmonome
# https://monome.org/docs/grid-studies/python/
#import monome

client = "APC40"
port = "APC40"

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

class ReadLoop:
    seq = sequencer.SequencerRead(sequencer_resolution=120)
    seq.subscribe_port(0, 0)
    seq.start_sequencer()
    while True:
      event = seq.event_read()
      if event is not None:
          print event

class WriteLoop:
    seq = sequencer.SequencerWrite(sequencer_resolution=pattern.resolution)
    seq.subscribe_port(client, port)
    seq.start_sequencer()
    for event in events:
        buf = seq.event_write(event, False, False, True)
        if buf == None:
            continue
        if buf < 1000:
            time.sleep(.5)
    while event.tick > seq.queue_get_tick_time():
        seq.drain()
        time.sleep(.5)

apc40_x = [1,2,3,4,5,6,7,8] # MIDI Channel
apc40_y = [53,54,55,56,57,52,51,50] # MIDI note number

def set_mode(m_type):
    if (m_type == 1):
        sysex = [0xF0,0x47,0x00,0x73,0x60,0x00,0x04,0x41,0x01,0x01,0x00,0xF7]
        midi.SysexEvent(data=sysex)
    if (m_type == 2):
        sysex = [0xF0,0x47,0x00,0x73,0x60,0x00,0x04,0x42,0x01,0x01,0x00,0xF7]
        midi.SysexEvent(data=sysex)
    else:
        sysex = [0xF0,0x47,0x00,0x73,0x60,0x00,0x04,0x40,0x01,0x01,0x00,0xF7]
        midi.SysexEvent(data=sysex)

def midi_to_monome(event):
    x = event[1]
    y = apc40_y.index(event[0]) + 1
    state = event[2]
    return [x,y,state]

set_mode(mode["ableton mode"])

print midi_to_monome([52,3,0])

# initialize monome
# https://monome.org/docs/osc/
# here's the server
# https://github.com/monome/serialosc/blob/master/src/serialosc-device/server.c
monome = []
