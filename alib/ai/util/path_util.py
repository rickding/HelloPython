import logging

from ai.util.file_util import temp_path, file_path, mk_dir

log = logging.getLogger(__name__)


def model_path(file):
    return file_path(temp_path('model'), file)


def image_path(file):
    return file_path(temp_path('image'), file)


def video_path(file):
    return file_path(temp_path('video'), file)


def face_dir():
    path = temp_path('face')
    mk_dir(path)
    return path


def face_path(file, sub_path=None):
    path = face_dir()
    if sub_path:
        path = temp_path(sub_path)
        mk_dir(path)

    return file_path(path, file)


def output_path(file):
    path = temp_path('processed')
    mk_dir(path)
    return file_path(path, file)
