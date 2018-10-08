import logging

import cv2
import face_recognition

from ai.face.path_util import image_path

log = logging.getLogger(__name__)


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


def mark_names(frame, face_locations, face_names, scale=4):
    if frame is None or len(face_locations) != len(face_names):
        return frame

    # Label the faces
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        # Scale back
        if scale > 1:
            top *= scale
            right *= scale
            bottom *= scale
            left *= scale

        # Draw a box
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with name below the face
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

    return frame
