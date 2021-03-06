import os


class Config(object):
    STATIC_FOLDER = os.environ.get('STATIC_FOLDER') or 'templates/'

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'powerful secret key'
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY') or 'a csrf secret key'

    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'application/resource/'
    SPECTROGRAM_FOLDER = os.environ.get('SPECTROGRAM_FOLDER') or 'spectrograms/'
    PATH_TO_SPECTROGRAM_FOLDER = os.environ.get('PATH_TO_SPECTROGRAM_FOLDER') or "application/templates/"
    MAX_CONTENT_LENGTH = os.environ.get('MAX_CONTENT_LENGTH') or 100 * 1024 * 1024
    ALLOWED_EXTENSIONS = os.environ.get('ALLOWED_EXTENSIONS') or {'mp3', 'wav', 'ogg', 'flack'}
