#!/usr/bin/env python

import time

import numpy as np
import pybullet

import skrobot

# initialize robot
robot = skrobot.models.pr2.PR2()
interface = skrobot.interfaces.PybulletRobotInterface(robot)

pybullet.resetDebugVisualizerCamera(
    cameraDistance=1.5,
    cameraYaw=45,
    cameraPitch=-45,
    cameraTargetPosition=(0, 0, 0.5),
)
print('==> Initialized PR2 Robot on PyBullet')
for _ in range(100):
    pybullet.stepSimulation()
time.sleep(3)
    
# reset pose
print('==> Moving to Reset Pose')
robot.reset_manip_pose()
interface.angle_vector(robot.angle_vector(), realtime_simulation=True)
interface.wait_interpolation()
print('==> end wait_interpolation')
