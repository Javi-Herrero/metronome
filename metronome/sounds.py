from synthesizer import Player, Synthesizer, Waveform
import time


player = Player()
player.open_stream()

synth = {
    '1': Synthesizer(
          osc1_waveform=Waveform.sine,
          osc1_volume=1.0,
          use_osc2=False
        ),

    '2': Synthesizer(
          osc1_waveform=Waveform.square,
          osc1_volume=.25,
        )
}


def sound(beat_length, current_beat, current_subdivision):

  sound_length = {
    'long': (beat_length / 10) if beat_length < 1.2 else 0.06,
    'short': 0.005
  }
  #print(sound_length)
  print(sound_length['long'] )

  sound_set = {
    '1': [2500, 1000, 10000],
    '2': [2000, 1000, 1000],
    '3': [2500, 1000, 10000],
    '4': [2500, 1000, 10000]
  }

  click_sounds = {
    'one': (synth['1'].generate_constant_wave(sound_set['1'][0], sound_length['long'] )),
    'beat': (synth['1'].generate_constant_wave(sound_set['1'][1], sound_length['long'] )),
    'subdiv': (synth['2'].generate_constant_wave(sound_set['1'][2], sound_length['short'] )),
  }

  if current_beat == 0 and current_subdivision == 1:
    player.play_wave(click_sounds['subdiv'])
    player.play_wave(click_sounds['one'])

  elif current_subdivision != 1:
    player.play_wave(click_sounds['subdiv'])

  else:
    player.play_wave(click_sounds['subdiv'])
    player.play_wave(click_sounds['beat'])
