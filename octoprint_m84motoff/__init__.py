# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin

class M84MotOffPlugin(octoprint.plugin.RestartNeedingPlugin):
	def rewrite_m18(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
		if gcode and gcode == "M18":
	 		cmd = "M84"
		return cmd,

	def get_update_information(self):
		return dict(
			m84motoff=dict(
				displayName="M84 Motors Off",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="ntoff",
				repo="OctoPrint-M84MotOff",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/ntoff/OctoPrint-M84MotOff/archive/{target_version}.zip"
			)
		)
        
__plugin_name__ = "M84 Motors Off"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = __plugin_implementation__ = M84MotOffPlugin()
    
	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.comm.protocol.gcode.queuing": __plugin_implementation__.rewrite_m18,
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}