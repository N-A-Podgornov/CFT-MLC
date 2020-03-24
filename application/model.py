from config import Config
import json
import plotly
import plotly.graph_objects as go
import numpy as np


# import pydub
# import librosa


class Model(object):

    def __init__(self, filename):
        self.filename = filename

    def print_fn(self):
        print(Config.UPLOAD_FOLDER + self.filename)

        # sound = pydub.AudioSegment.from_mp3(Config.UPLOAD_FOLDER + self.filename)
        # print(sound.raw_data)

        # y, sr = librosa.load(librosa.util.example_audio_file())
        # D = np.abs(librosa.stft(y))
        # print(D)

    @staticmethod
    def create_plot():
        count = 500
        xScale = np.linspace(0, 100, count)
        yScale = np.random.randn(count)

        # Create a trace
        trace = go.Scatter(x=xScale, y=yScale)
        data = [trace]

        graph_json = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
        return graph_json
