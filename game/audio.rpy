init:
  $ renpy.music.register_channel("ambient", mixer=None, loop=True, stop_on_mute=True, buffer_queue=True)

  define audio.father_cough_silent = '<from 3 to 5>assets/sounds/father_coughing.opus'
  define audio.father_cough_loud = '<from 8 to 11>assets/sounds/father_coughing.opus'
  define audio.father_cough_silent_with_pause = ['<silence 0.5>', '<from 3 to 5>assets/sounds/father_coughing.opus']
  define audio.cucu_cugu_scream = 'assets/sounds/cucu_cugu_scream.opus'
  define audio.door_opening = 'assets/sounds/door.opus'
  define audio.rain = 'assets/sounds/rain.opus'
