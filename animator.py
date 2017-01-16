from vector import Vector
from trajectory import Trajectory
from cube import Cube
from camera import Camera
from ankidata import repetition_iterator, get_date_from_anki_day
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Animator:
    def __init__(self):
        self.cubes = dict() # Mapping from card id to cube object
        self.stacks = dict() # Mapping from day to stack
        self.camera = Camera()
        # self.stacks = []
        # self.stacks_offset = 0
        self.current_day = 0
        self.time = 0
        self.animation_end_time = 0
        self.animation_duration = 3
        self.repetition_days = repetition_iterator()
        self.current_day_animations = []
        self.cardcount = 0
        self.max_animation_duration = 0.5

        self.next_day()



    def update(self, elapsed_time):
        self.time += elapsed_time
        if self.time >= self.animation_end_time:
            self.next_day()
        self.camera.update_position(elapsed_time)

    def next_day(self):

        # for cube in self.currently_animating:
        #     cube.trajectory = None # Reset previous animations
        self.current_day_animations = [] # Clear list of the current day of animations

        try:
            day, repetitions = self.repetition_days.next()
            self.current_day = day
        except StopIteration:
            print "Finished!"
            return

        print day

        cards_to_remove = []

        # Make movements of repetitions
        for card, interval in repetitions:
            if card not in self.cubes:
                current_stack = day - 40
                self.add_cube(card, current_stack) # Add new cubes to some distance to the left so that they can be introduced by jumping to stack 1
                self.cardcount += 1
            else:
                current_stack = day
            # if interval == 0:
            #     if self.cubes[card] in self.stacks[day]:
            #         self.stacks[day].remove(self.cubes[card])  # Remove cube from old stack
            # else:
            #     cards_to_remove.append(card)
            if current_stack in self.stacks and self.cubes[card] in self.stacks[current_stack]:
                self.stacks[current_stack].remove(self.cubes[card])  # Remove cube from old stack
            self.cubes[card].set_color_from_interval(interval)
            self.move_cube(self.cubes[card], day + interval) # Move cube to new stack

        # Remove cubes from previous stack
        # for card in cards_to_remove:
        #     if self.cubes[card] in self.stacks[day]:
        #         self.stacks[day].remove(self.cubes[card]) # Remove cube from old stack

        self.animation_duration = self.max_animation_duration#len(self.current_day_animations) and min(self.max_animation_duration, max([cube.trajectory and cube.trajectory.duration for cube in self.current_day_animations])) or self.max_animation_duration
        if self.animation_duration == None:
            self.animation_end_time = self.time
        else:
            self.animation_end_time = self.time + self.animation_duration

        # TODO: Handle cards that were not repeated (and are therefore located at "negative" days)

        # Remove stack for the finished day

        #del self.stacks[day]

    def add_cube(self, card_id, day):
        if day not in self.stacks:
            self.stacks[day] = []
        self.cubes[card_id] = Cube(card_id, Vector(day, len(self.stacks[day])))
        self.stacks[day].append(self.cubes[card_id])

    def move_cube(self, cube, to_day):
        if to_day not in self.stacks:
            self.stacks[to_day] = []
        next_position = Vector(to_day, len(self.stacks[to_day]))
        cube.trajectory = Trajectory(cube.position, next_position, self.time)
        cube.position = next_position
        self.current_day_animations.append(cube)
        self.stacks[to_day].append(cube)

    def get_date(self):
        return get_date_from_anki_day(self.current_day)

    def get_cardcount(self):
        return self.cardcount