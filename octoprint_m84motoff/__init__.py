# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin

class M84MotOffPlugin(octoprint.plugin.RestartNeedingPlugin):
    def rewrite_m18(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
	    if gcode and gcode == "M18":
	        cmd = "M84"
	    return cmd,
        
__plugin_name__ = "M84 Motors Off"
__plugin_implementation__ = M84MotOffPlugin()
__plugin_hooks__ = {
        "octoprint.comm.protocol.gcode.queuing": __plugin_implementation__.rewrite_m18
    }  
