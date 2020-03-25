import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from config import Config


class Model(object):

    def __init__(self, filename):
        self.filename = filename

    def get_spectrogram(self):
        filename = Config.UPLOAD_FOLDER + self.filename

        data, samplerate = librosa.load(filename)
        D = np.abs(librosa.stft(data))

        librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max), y_axis='log', x_axis='time')
        plt.title('Power spectrogram')
        plt.colorbar(format='%+2.0f dB')
        plt.tight_layout()

        return plt
