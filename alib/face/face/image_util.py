import logging

import cv2
import face_recognition

from ai.util.path_util import image_path

log = logging.getLogger(__name__)


def read_image(file_path):
    if file_path is None:
        return None
    return cv2.imread(file_path)


def get_known_faces():
    # Load faces
    known_names = ['Lin-Manuel Miranda', 'Alex Lacamoire', 'Biden', 'Obama']
    known_faces = [
        face_recognition.face_encodings(face_recognition.load_image_file(
            image_path('lin-manuel-miranda.png')))[0],
        face_recognition.face_encodings(face_recognition.load_image_file(
            image_path('alex-lacamoire.png')))[0],
        face_recognition.face_encodings(face_recognition.load_image_file(
            image_path('biden.jpg')))[0],
        face_recognition.face_encodings(face_recognition.load_image_file(
            image_path('obama.jpg')))[0],
    ]
    return known_names, known_faces
