"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time
from rtmidi.midiutil import open_midiinput
from rtmidi.midiconstants import NOTE_ON, NOTE_OFF

from pythonosc import osc_message_builder
from pythonosc import udp_client

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
  help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=12289,
  help="The port the OSC server is listening on")
args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)

apc40_y = [53,54,55,56,57,52,51,50,49,48] # MIDI note numbers in order, top to bottom, each row

def monome_grid_key(event, data=None):
    message, deltatime = event

    if message[0] & 0xF0 == NOTE_ON:
        status, note, velocity = message
        channel = (status & 0xF) + 1
        x = channel
        y = apc40_y.index(note) + 1
        state = 1
        print("/monome/grid/key %s %s %s" % (x, y, state))
        client.send_message("/monome/grid/key", [x, y, state])
    elif message[0] & 0xF0 == NOTE_OFF:
        status, note, velocity = message
        channel = (status & 0xF) + 1
        x = channel
        y = apc40_y.index(note) + 1
        state = 0
        print("/monome/grid/key %s %s %s" % (x, y, state))
        client.send_message("/monome/grid/key", [x, y, state])

if __name__ == "__main__":
  with open_midiinput(1, client_name='noteon2osc')[0] as midiin:
    midiin.set_callback(monome_grid_key)

    while True:
      time.sleep(1)
