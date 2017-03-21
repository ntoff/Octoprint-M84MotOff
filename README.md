# M84 Motors Off

Change the command sent by the "Motors off" button in OctoPrint's "control" tab to issue M84, for compatibility with Repetier firmware, instead of M18. The plugin makes no visual changes to the octoprint UI.

Please note: This plugin works by intercepting the gcode command M18 during the queueing stage, and rewriting it as M84 before sending it to the printer. This means that even if you enter M18 in the manual gcode entry terminal box, it will be sent to the printer as M84.

## Install
Install from the plugin manager or manually using this URL:

    https://github.com/ntoff/OctoPrint-M84MotOff/archive/master.zip

