# monome-apc40
Glue to make the Akai APC40 work with Monome OSC software

[Video proof of concept](https://youtu.be/bNDq6Z38rRI)

## Installation

git clone --recursive <url>
pacman -S python2 python2-pip swig alsa-lib
pip install virtualenv
python -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
cd python-midi
python setup.py install
