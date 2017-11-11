"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=8000,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  while True:
    client.send_message("/monome/grid/led/all", 1)
    time.sleep(0.5)
    client.send_message("/monome/grid/led/all", 0)
    time.sleep(0.5)
    client.send_message("/monome/grid/led/set", [1, 1, 1])
    client.send_message("/monome/grid/led/set", [8, 10, 1])
    client.send_message("/monome/grid/led/set", [8, 1, 1])
    client.send_message("/monome/grid/led/set", [1, 10, 1])
    time.sleep(0.5)
    client.send_message("/monome/grid/led/set", [1, 1, 0])
    client.send_message("/monome/grid/led/set", [8, 10, 0])
    client.send_message("/monome/grid/led/set", [8, 1, 0])
    client.send_message("/monome/grid/led/set", [1, 10, 0])
    time.sleep(0.5)
    for x in range(8):
        for y in range(10):
            time.sleep(0.2)
            client.send_message("/monome/grid/led/set", [x + 1, y + 1, 1])
            time.sleep(0.2)
            client.send_message("/monome/grid/led/set", [x + 1, y + 1, 0])
