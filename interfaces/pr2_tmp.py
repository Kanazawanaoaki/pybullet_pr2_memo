import importlib

import numpy as np

from skrobot.interfaces import PybulletRobotInterface

class PR2TMPRobotInterface(PybulletRobotInterface):
    """pr2 robot interface."""

    def __init__(self, *args, **kwargs):
        super(PR2TMPRobotInterface, self).__init__(*args, **kwargs)

    def wait_interpolation(self, controller_type=None, timeout=0):
        """Overwrite wait_interpolation
        Overwrite for pr2 because some joint is still moving after joint-
        trajectory-action stops.
        Parameters
        ----------
        controller_type : None or string
            controller to be wait
        timeout : float
            max time of for waiting
        Returns
        -------
            return values are a list of is_interpolating for all controllers.
            if all interpolation has stopped, return True.
        """
        super(PR2TMPRobotInterface, self).wait_interpolation(
            controller_type, timeout)
        while not rospy.is_shutdown():
            self.update_robot_state(wait_until_update=True)
            if all(map(lambda j: j.name in self.ignore_joint_list or
                       abs(j.joint_velocity) < 0.05
                       if isinstance(j, RotationalJoint) else
                       abs(j.joint_velocity) < 0.001,
                       self.robot.joint_list)):
                break
        # TODO(Fix return value)
        return True

