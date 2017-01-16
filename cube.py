from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from vector import Vector
from trajectory import Trajectory
import math

class Cube:
    color_highest = math.log(3650)

    def __init__(self, card_id, position):
        self.card = card_id
        self.color = QtGui.QColor(Qt.white)
        self.position = position
        self.trajectory = None
        # self.trajectory = Trajectory(Vector(0, 0), Vector(60, 0), math.pi / 4)
        # self.position = self.trajectory.start

    def set_color_from_interval(self, interval):
        if interval <= 0:
            self.color.setHsl(0, 160, 122)
        else:
            luminance = 255*(1 - max(0, min((math.log(interval)-1) / (Cube.color_highest-1), 1)))
            self.color.setHsl(215, 186, luminance)
            # self.color = QtGui.QColor.fromHsl(215, 186, luminance)#luminance)

    def get_position(self, t):
        if self.trajectory is None:
            return self.position
        return self.trajectory.position_at_time(t)