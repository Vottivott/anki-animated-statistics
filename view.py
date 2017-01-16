#!/usr/bin/python
# -*- coding: utf-8 -*-

from vector import Vector
from trajectory import Trajectory
from cube import Cube
from camera import Camera
from animator import Animator

import time
import datetime

"""
ZetCode PyQt4 tutorial

In the example, we draw randomly 1000 red points
on the window.

author: Jan Bodnar
website: zetcode.com
last edited: September 2011
"""

import sys, random
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

        self.t = 0

        self.frames_per_second = 24

        self.camera = Camera()

        self.animator = Animator()

        self.fps_stats = []
        self.fps_stats_samples = 40

    def initUI(self):
        # self.setGeometry(300, 300, 280, 170)
        self.setMinimumWidth(1280)
        self.setMinimumHeight(720)
        self.setWindowTitle('Animated Statistics')
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        # self.drawPoints(qp)
        self.drawCubes(qp)
        self.drawText(qp, self.animator.current_day, self.animator.get_date(), self.animator.get_cardcount())
        qp.end()

    def drawText(self, qp, day, date, cards):
        date_str = "Day " + str(day+1) + "\n" + str(date)
        cards_str = "Added cards: " + str(cards)

        debug_str = "FPS: %0.f" % (sum(self.fps_stats) / len(self.fps_stats))
        qp.drawText(self.width() - 200, 10, 190, 200, QtCore.Qt.AlignRight, date_str + "\n" + cards_str + "\n" + debug_str)



    def closeEvent(self, QCloseEvent):
        app = QtGui.QApplication(sys.argv)
        self.close()


    def drawCubes(self, qp):
        qp.setPen(QtCore.Qt.red)
        qp.setPen(QPen(QBrush(Qt.red), 2.5, Qt.DashLine))
        size = self.size()

        for cube in self.animator.cubes.values():
            self.drawCube(qp, cube)
            #c = Cube(0, cube.trajectory.end)
            #c.color = QtCore.Qt.black
            #self.drawCube(qp, c)




    def drawCube(self, qp, cube):
        size = self.size()
        # qp.setPen(cube.color)
        # qp.setPen(QPen(QBrush(Qt.red), 2.5, Qt.DashLine))
        qp.setPen(QPen(QBrush(cube.color), 2))

        pos = self.camera.transform_position(cube.get_position(self.animator.animation_time))
        rectangle = QtCore.QRectF(pos.x, pos.y, 1.0/self.camera.scale, 1.0/self.camera.scale)
        qp.drawRect(rectangle)

    def keyPressEvent(self, QKeyEvent):
        key = QKeyEvent.key()
        if key == QtCore.Qt.Key_Left:
            self.camera.position.x -= 10
        if key == QtCore.Qt.Key_Right:
            self.camera.position.x += 10
        if key == QtCore.Qt.Key_Up:
            self.camera.position.x -= 30
        if key == QtCore.Qt.Key_Down:
            self.camera.position.x += 30

    def drawPoints(self, qp):
        qp.setPen(QtCore.Qt.red)
        size = self.size()

        for i in range(8000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)

    def update_fps_stats(self, elapsed_time):
        fps = 1.0 / elapsed_time
        if len(self.fps_stats) > self.fps_stats_samples:
            self.fps_stats.pop(0)
        self.fps_stats.append(fps)

    def startAnimation(self):
        last_time = time.time()
        for i in range(1000000):
            current_time = time.time()
            elapsed_time = (current_time - last_time) * 100#23#4#3#0
            self.update_fps_stats(current_time - last_time)
            last_time = current_time
            self.update()
            QtGui.QApplication.processEvents()
            self.animator.update(elapsed_time)
            self.t += elapsed_time



def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.startAnimation()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()