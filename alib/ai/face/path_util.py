import logging

from ai.util.file_util import temp_path, full_path, mk_dir

log = logging.getLogger(__name__)


def model_path(file):
    return full_path(temp_path('model'), file)


def image_path(file):
    return full_path(temp_path('image'), file)


def video_path(file):
    return full_path(temp_path('video'), file)


def face_path(file, sub_path=None):
    path = temp_path()
    for sub_dir in ['face', sub_path]:
        if sub_dir:
            path = temp_path(sub_dir)
            mk_dir(path)

    return full_path(path, file)


def output_path(file):
    path = temp_path('processed')
    mk_dir(path)
    return full_path(path, file)
