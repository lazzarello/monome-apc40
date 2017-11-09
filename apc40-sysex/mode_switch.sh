# sysex for "ableton mode" initialization

# enable midi dump on APC40 port
aseqdump -p 24:0 

device_enquiry = "F0 7E 00 06 01 F7"

# get device specific sysex response

# amidi -p hw:2,0,0 -S ${device_enquiry}
amidi -p hw:2,0,0 -S "F0 7E 00 06 01 F7"

device_response = "F0 7E 00 06 02 47 73 00 19 00 01 00 02 00 7F 7F 7F 7F 00 4B 02 01 02 01 00 00 02 03 08 00 00 07 06 00 F7"

device_id = "00"
# 40 for generic MIDI
# 42 for "alt ableton"
device_mode = "41"
app_version_high = "01"
app_version_low = "01"
bugfix_level = "00"

#set_mode_1 = "F0 47 ${device_id} 73 60 00 04 ${device_mode} ${app_version_high} ${app_version_low} ${bugfix_level} F7"
set_mode_1 = "F0 47 00 73 60 00 04 41 01 01 00 F7"
#amidi -p hw:2,0,0 -S ${set_mode_1}
amidi -p hw:2,0,0 -S "F0 47 00 73 60 00 04 41 01 01 00 F7"
amidi -p hw:2,0,0 -S "F0 47 00 73 60 00 04 40 01 01 00 F7"
