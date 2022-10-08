# """
# C:/Scripts/Nuke>
# C:/'Program Files'/Nuke13.2v4/Nuke13.2.exe --nukex -x -t
# runonstart.py
# template.nk
# template_mod.nk
# 1,1
# """


# function vars
project_dir = "G:/Shared drives/TriplegangersGroom_ext/Groom_INTERNAL/SimonYuen/maya/base_delta/images/dh_coil_0.5c0.1r_dh_coil_0.5c3.6r_dh_noise_0.1freq_0.6mag_0.5corr_dh_noise_0.1freq_4.6mag_0.5corr/"
json_file = "test.json"


import nuke
import sys
# import os
import json

# from config import *

with open(project_dir+json_file) as infile:
    metadata = json.load(infile)


nuke.scriptOpen("C:/Scripts/nuke/template.nk")

nuke.toNode("root")['project_directory'].setValue(metadata["project_dir"])
for knob in ['last', 'origlast']:
    nuke.toNode("INPUT_SEQ")[knob].setValue(metadata["last_frame"])
nuke.toNode("root")['last_frame'].setValue(metadata["last_frame"])
# for knob in ['rows', 'columns', 'width', 'height']:
#     nuke.toNode('ContactSheet1')[knob].setValue(metadata["last_frame"])
nuke.toNode('ContactSheet1')['rows'].setValue(metadata['rows'])
nuke.toNode('ContactSheet1')['columns'].setValue(metadata['columns'])
nuke.toNode('ContactSheet1')['width'].setValue(metadata['columns']*250)
nuke.toNode('ContactSheet1')['height'].setValue(metadata['rows']*250)

nuke.scriptSave(sys.argv[1])


