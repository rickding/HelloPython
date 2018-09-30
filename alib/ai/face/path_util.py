import logging

from ai.util.file_util import temp_path, full_path

log = logging.getLogger(__name__)


def model_path(file):
    return full_path(temp_path(), file)


def image_path(file):
    return full_path(temp_path(), file)
