# monome-apc40
Glue to make the Akai APC40 work with Monome OSC software

[Video demo of scripts running](https://youtu.be/Ahpgsh8qhOI)

## Installation

### Arch Linux

```
git clone --recursive <url>
pacman -S python python-pip swig alsa-lib alsa-utils alsa-tools
pip install virtualenv
python -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

### macOS

```
git clone --recursive <url>
brew install python3 pip3
pip3 install virtualenv
python3 -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Running

There are two scripts, `midiin_server.py` and `midiout_server.py`. Each is run in a shell. Each requires the shell to be in the virtualenv.

## Tests

By default running `python midiout_server.py` starts an OSC server on
localhost:8000

To test midi output connectivity, run `python test_client.py` in a different shell and
observe the server output.

## Python versions and C bindings

* [RTMidi C++ lib](http://www.music.mcgill.ca/~gary/rtmidi/) looks like the way to go. 
* There are [python bindings](https://github.com/SpotlightKid/python-rtmidi) with many good examples.
* It
[python-osc](https://github.com/attwad/python-osc) only works with python 3, despite installing in a python 2.7 virtualenv.
