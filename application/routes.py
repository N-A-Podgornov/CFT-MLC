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
    Model(filename).print_fn()
    return render_template('response.html', plot=Model.create_plot())
