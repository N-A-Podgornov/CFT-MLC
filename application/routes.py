import os
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


@app.route('/submit', methods=['GET', 'POST'])
def submit():
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
    out_fn = os.path.join(Config.UPLOAD_FOLDER, in_fn + ".png")
    # out_fn1 = os.path.join("application/templates/images/", in_fn + ".png")  # todo del
    # out_fn2 = os.path.join("images/", in_fn + ".png")  # todo del

    Model(filename).get_spectrogram().savefig(out_fn)
    return render_template('response.html', spectrogram=out_fn)
