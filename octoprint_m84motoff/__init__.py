# coding=utf-8

import octoprint.plugin

class M84MotOffPlugin(octoprint.plugin.OctoPrintPlugin):
        
    def rewrite_m18(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
        if gcode and gcode == "M18":
            cmd = "M84"
        return cmd,

__plugin_name__ = "M84 Motors Off"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = M84MotOffPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.comm.protocol.gcode.queuing": __plugin_implementation__.rewrite_m18
    }
    