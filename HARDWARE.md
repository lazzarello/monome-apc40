# MIDI to Monome Serial adapter

## Parts

  * A circuit to act as USB host, most likely [USB_Host_Shield_2.0](https://github.com/felis/USB_Host_Shield_2.0)?
  * A microcontroller to load firmware, [most likely a Teensy++ 2.0](https://www.pjrc.com/store/teensypp.html)
  * Voltage regulator for Teensy [to drop to 3.3V](https://www.pjrc.com/store/mcp1825.html)
  * Some kind of project box enclosure

## Firmware requirements
  * Recognize an attached [USB MIDI device](https://github.com/felis/USB_Host_Shield_2.0#midi-library).
  * Implement the [Monome serial protocol](https://github.com/monome/mk/blob/master/firmware/default/mk.c)
  * Translate [MIDI Note On/Off](https://github.com/lazzarello/monome-apc40/blob/master/midiin_server.py) and CC delta (encoder) to the Monome serial protocol
  * Translate Monome serial protocol to [MIDI Note On/Off](https://github.com/lazzarello/monome-apc40/blob/master/midiout_server.py) and MIDI CC if there's an LED ring
  * USB mini [device port to connect to host](https://www.pjrc.com/teensy/td_serial.html) and send Monome serial
