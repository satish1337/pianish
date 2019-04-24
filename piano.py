

#!/usr/bin/env python3

import numpy as np
from scipy.io import wavfile
import scikits.audiolab


def save_sound(frequency=440):
    sampleRate = 44100
    length = 1

    t = np.linspace(0, length, sampleRate * length)  #  Produces a 1 second Audio-File
    y = np.sin(frequency * 2 * np.pi * t)  #  Has frequency of 440Hz
    data = np.random.uniform(-1,1,2200)
    scikits.audiolab.play(y, fs=44100)
    #wavfile.write('Sine-{}.wav'.format(frequency), sampleRate, y)


#save_sound(frequency=432)


def get_piano_sounds():
    ref_point = 432
    for i in range(12):
        save_sound(frequency=ref_point)
        ref_point = ref_point*pow(2, 1/12.0)


get_piano_sounds()
