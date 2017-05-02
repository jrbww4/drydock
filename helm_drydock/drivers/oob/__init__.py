# Copyright 2017 AT&T Intellectual Property.  All other rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# OOB:
# sync_hardware_clock
# collect_chassis_sysinfo
# enable_netboot
# initiate_reboot
# set_power_off
# set_power_on
import helm_drydock.objects.fields as hd_fields
import helm_drydock.error as errors

from helm_drydock.drivers import ProviderDriver

class OobDriver(ProviderDriver):

    def __init__(self, **kwargs):
        super(OobDriver, self).__init__(**kwargs)

        self.supported_actions = [hd_fields.OrchestratorAction.ConfigNodePxe,
                                  hd_fields.OrchestratorAction.SetNodeBoot,
                                  hd_fields.OrchestratorAction.PowerOffNode,
                                  hd_fields.OrchestratorAction.PowerOnNode,
                                  hd_fields.OrchestratorAction.PowerCycleNode,
                                  hd_fields.OrchestratorAction.InterrogateNode]

        self.driver_name = "oob_generic"
        self.driver_key = "oob_generic"
        self.driver_desc = "Generic OOB Driver"

    def execute_task(self, task_id):
        task = self.state_manager.get_task(task_id)
        task_action = task.action

        if task_action in self.supported_actions:
            return
        else:
            raise DriverError("Unsupported action %s for driver %s" %
                (task_action, self.driver_desc))
