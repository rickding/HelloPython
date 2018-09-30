import logging

import cv2

from ai.face.path_util import image_path

log = logging.getLogger(__name__)


def get_video_file(file_name):
    video_input = cv2.VideoCapture(image_path(file_name))
    video_len = int(video_input.get(cv2.CAP_PROP_FRAME_COUNT))
    return video_input, video_len


def get_video_capture():
    return cv2.VideoCapture(0), 1
