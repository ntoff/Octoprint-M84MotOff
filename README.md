# OctoPrint-M84MotOff

Change the "Motors off" button in OctoPrint's "control" tab to issue M84 instead of M18 for compatibility with Repetier firmware.

Please note, this plugin works by intercepting the gcode command M18 and rewriting it as M84. This means that even if you enter M18 in the manual gcode entry terminal box, it will be sent to the printer as M84.

## Setup

Install manually using this URL:

    https://github.com/ntoff/OctoPrint-M84MotOff/archive/master.zip


