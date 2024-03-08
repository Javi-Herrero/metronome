import sounds
import animations
import time

from kivy.uix.button import Button

def apply_settings(self, instance):
        subdivisions = instance['subdivisions']
        if instance['subdivisions'] > 1:
            self.root.ids.label.status = instance['tempo']
            animations.draw_subdivisions(self, instance['subdivisions'])
        else:
            self.root.ids.ball.canvas.remove_group('line_group')

def animate(self, instance, bpm, i, subdivisions, current_beat):
    print('io')
    if subdivisions > 1:
        animations.anim2_subdiv(self, instance, bpm, i, subdivisions)
    else:
        animations.anim1(self, instance, bpm, i, subdivisions)

    animations.anim3_beats(self, current_beat)

cols = 1
def add_beats(self, instance):
    button = Button(text=str(self.cols + 1), background_color = (0, 0, 0, 0))
    layout = self.root.ids.beats

    if instance == '+':
        if self.cols == 0:
            layout.remove_widget(self.root.ids.dumb)

        self.cols = self.cols + 1
        layout.add_widget(button)

    elif self.cols >= 2:
        self.cols = self.cols - 1
        layout.remove_widget(self.root.ids.beats.children[0])

    layout.cols = self.cols and  8 if self.cols > 8 else self.cols

beat_count = 0
i = 0
def reset_count(self, slider_move):
    self.i = 0
    animations.Animation.cancel_all(self.root.ids.ball)
    self.root.ids.ball.angleStart = 0
    self.root.ids.ball.angleEnd = 0
    if not slider_move:
        self.beat_count = 0

def hartbeat(self, bpm, subdivisions, current_beat):
        self.animate(self.root.ids.ball, bpm, self.i, subdivisions, current_beat)
        sounds.sound(bpm)

        self.startMetro()

