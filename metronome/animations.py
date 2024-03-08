from kivy.animation import Animation
from kivy.graphics import *

from math import cos, sin, radians

def anim1(self, instance, beat_length, i, subdivisions):
    ball = self.root.ids.ball
    initial_angle = (i % 2) * 360
    if initial_angle == 0:
        end_angle = -360
    else:
        end_angle = 0

    ball.angleEnd = initial_angle
    ball.angleStart = 0

    animation = Animation( angleEnd = end_angle, d = beat_length, t = 'linear')
    animation.start(ball)

def anim2_subdiv(self, instance, beat_length, i, subdivisions):
    ball = self.root.ids.ball
    current_subdivision = i % subdivisions + 1
    ball.angleStart = 0
    ball.angleEnd = 0
    if i % (subdivisions * 2)>= subdivisions:
        start_angle = -360
    else:
        start_angle = 0

    ball.angleStart = start_angle
    ball.angleEnd = current_subdivision * (-360 / subdivisions)

def anim3_beats(self, current_beat):
    beats = self.root.ids.beats
    invert_beat = (len(beats.children) - current_beat) - 1
    for step in beats.children:
        step.background_color = (1, 0, 1, 0)
    beats.children[invert_beat].background_color = (1, 1, 1, 1 )


def draw_subdivisions(self, subdivisions):
    ball = self.root.ids.ball
    subdivisions = int(subdivisions)
    position = ball.centerPos
    size = ball.rize

    # Remove previously drawn lines with the specified id
    ball.canvas.remove_group('line_group')

    with ball.canvas:

            for i in range(subdivisions):
                start_angle = radians(i * (360.0 / subdivisions)) + radians(90)

                # Calculate the starting and ending points of the segment
                x1 = position[0] + size[0] / 2 * cos(start_angle) + size[0] / 2
                y1 = position[1] + size[0] / 2 * sin(start_angle) + size[0] / 2

                Color(0, 0, 0, 1)
                line_group = Line(group='line_group', width=3)

                # Draw a line segment
                line_group.points += [position[0] + size[0] / 2, position[1] + size[0] / 2, x1, y1]

def cancelAnim(self):
    Animation.stop(self.root.ids.ball)