from vector import Vector
from math import sqrt, sin, cos, tan, pi

"""
Class that represents the trajectory movement between two positions
"""

class Trajectory:
    gravity = 9.82 * 30 * 0.13

    def __init__(self, start, end, angle=pi/4):
        """
        Creates a new Trajectory object
        :param start: the start position as a Vector
        :param end: the end position as a Vector
        :param angle: the angle between the ground and the initial velocity vector
        """
        self.start = start
        self.end = end
        if start.x == end.x:
            speed = 3
            self.initial_velocity = Vector(0, speed)
            self.duration = 2 * speed / Trajectory.gravity
        else:
            self.initial_velocity = self.calculate_initial_velocity(angle)
            self.duration = self.get_duration()

    def calculate_initial_velocity(self, angle):
        delta = self.end - self.start
        if delta.x < 0:
            return Vector(0, 10) # TODO: Fix
        to_be_squared = (Trajectory.gravity * delta.x**2)/(((tan(angle)*delta.x-delta.y)*(2*cos(angle)**2)))
        while to_be_squared < 0: # TODO: if to_be_squared is negative that means the equation has no solution, i.e. we need to raise the angle
            angle = min((pi/2 + angle)/2, angle + pi/30)
            to_be_squared = (Trajectory.gravity * delta.x**2)/(((tan(angle)*delta.x-delta.y)*(2*cos(angle)**2)))
        speed = sqrt(to_be_squared)
        return Vector(speed*cos(angle), speed*sin(angle))

    def position_at_time(self, t):
        if t >= self.duration:
            return self.end
        dx = t * self.initial_velocity.x
        dy = t * self.initial_velocity.y - t**2 * Trajectory.gravity / 2
        return self.start + Vector(dx, dy)

    def get_duration(self):
        delta = self.end - self.start
        if (self.initial_velocity.x == 0):
            return 1 #TODO: something sensible when jumping on place
        return delta.x / self.initial_velocity.x