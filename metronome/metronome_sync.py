from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.animation import Animation
import sounds


from kivy.app import App
from kivy.lang.builder import Builder

class Metronome(App):
    from utils import apply_settings
    from utils import animate
    from utils import add_beats
    from utils import reset_count

    from utils import i
    from utils import beat_count
    from utils import cols
    from utils import heartbeat

    other_task = None
    subdivisions = 1

    def build(self):
        return Builder.load_file('metro.kv')



    def startMetro(self):
        if sounds.beat_finished == False:
            self.heartbeat()

if __name__ == '__main__':
    Metronome().run()