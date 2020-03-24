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
        n = 100000
        fig = go.Figure(data=go.Scattergl(
            x=np.random.randn(n),
            y=np.random.randn(n),
            mode='markers',
            marker=dict(
                color=np.random.randn(n),
                colorscale='Viridis',
                line_width=1
            )
        ))

        graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graph_json
