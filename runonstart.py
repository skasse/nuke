# """
# C:\Scripts\Nuke>
# C:\'Program Files'\Nuke13.2v4\Nuke13.2.exe --nukex -i -t
# runonstart.py
# template.nk
# template_mod.nk
# """

import nuke
import sys
# import os

from config import *

nuke.scriptOpen(sys.argv[1])
# lastFrame:int = 80
knobs = ['last', 'origlast']
for knob in knobs:
    nuke.toNode("INPUT_SEQ")[knob].setValue(int(lastFrame))
nuke.toNode("root")['last_frame'].setValue(int(lastFrame))
nuke.scriptSave(sys.argv[2])


