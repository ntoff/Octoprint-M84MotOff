# coding=utf-8
from __future__ import absolute_import

def rewrite_m18(comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
    if gcode and gcode == "M18":
        cmd = "M84"
    return cmd,

__plugin_name__ = "M84 Motors Off"

__plugin_hooks__ = {
        "octoprint.comm.protocol.gcode.queuing": rewrite_m18
}

    
