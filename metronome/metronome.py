import time
import asyncio
import sounds
import math
import threading

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

    other_task = None
    subdivisions = 1


    def build(self):
        return Builder.load_file('metro.kv')

    def app_func(self):
        self.other_task = asyncio.ensure_future(self.waste_time_freely())

        async def run_wrapper():
            # we don't actually need to set asyncio as the lib because it is
            # the default, but it doesn't hurt to be explicit
            await self.async_run(async_lib='asyncio')
            print('App done')
            self.other_task.cancel()

        return asyncio.gather(run_wrapper(), self.other_task)

    async def waste_time_freely(self):
            try:
                while True:
                    if self.root is not None:
                        while  self.root.ids.btn1.state == 'down':
                            subdivisions = self.root.ids.subdiv.value
                            beat_length = (60  / int(self.root.ids.label.status)) / ( subdivisions )
                            current_subdivision = self.i % subdivisions + 1
                            beats = self.cols

                            if current_subdivision == 1 and beats != 0:
                                current_beat = self.beat_count % beats
                                self.beat_count += 1
                            # make sure we dont initialize the click with zero beats
                            if self.cols == 0:
                                current_beat = 1

                            threading.Thread(target=sounds.sound, args=(beat_length, current_beat, current_subdivision)).start()
                            self.animate(self.root.ids.ball, beat_length, self.i, subdivisions, current_beat)

                            self.i = self.i + 1
                            await asyncio.sleep(beat_length)

                    await asyncio.sleep(.001)

            except asyncio.CancelledError as e:
                print('Wasting time was canceled', e)
            finally:
                # when canceled, print that it finished
                print('Done wasting time')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Metronome().app_func())
    loop.close()