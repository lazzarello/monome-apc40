# monome-apc40
Glue to make the Akai APC40 work with Monome OSC software

[Video proof of concept](https://youtu.be/bNDq6Z38rRI)

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

## Tests

By default running `python server.py` starts an OSC server on
localhost:8000

To test connectivity, run `python client.py` in a different shell and
observe the server outpu

## Python versions and C bindings

[RTMidi C++ lib](http://www.music.mcgill.ca/~gary/rtmidi/) looks like the way to go.
python-osc only work with python 3, despite installing in a python 2.7 virtualenv.
