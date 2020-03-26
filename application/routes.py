import os
import shutil
from flask import render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
from config import Config
from application import app
from application.model import Model


@app.route('/')
def index():
    return redirect(url_for('submit'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in Config.ALLOWED_EXTENSIONS


def file_system_preparation():
    try:
        shutil.rmtree(path=Config.UPLOAD_FOLDER)
        shutil.rmtree(path=Config.PATH_TO_SPECTROGRAM_FOLDER + Config.SPECTROGRAM_FOLDER)
    except OSError:
        print("error :: failed to clean file system")

    try:
        os.mkdir(path=Config.UPLOAD_FOLDER)
        os.mkdir(path=Config.PATH_TO_SPECTROGRAM_FOLDER + Config.SPECTROGRAM_FOLDER)
    except OSError:
        print("error :: failed to prepare file system")


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    file_system_preparation()

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('response', filename=filename))

    return render_template('submit.html')


@app.route('/<filename>', methods=['GET'])
def response(filename):
    in_fn, fn_ex = os.path.splitext(filename)

    out_fn_w = os.path.join(Config.PATH_TO_SPECTROGRAM_FOLDER + Config.SPECTROGRAM_FOLDER, in_fn + ".png")
    out_fn_r = os.path.join(Config.SPECTROGRAM_FOLDER, in_fn + ".png")

    Model(filename).get_spectrogram().savefig(out_fn_w)
    return render_template('response.html', spectrogram=out_fn_r)
