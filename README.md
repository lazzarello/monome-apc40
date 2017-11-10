# monome-apc40
Glue to make the Akai APC40 work with Monome OSC software

[Video proof of concept](https://youtu.be/bNDq6Z38rRI)

## Installation

```
git clone --recursive <url>
pacman -S python python-pip swig alsa-lib alsa-utils alsa-tools
pip install virtualenv
python -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
cd python-midi
python setup.py install
```

## Python versions and C bindings

[RTMidi C++ lib](http://www.music.mcgill.ca/~gary/rtmidi/) looks like the way to go.
Python 3 looks like it should be a default.
