import logging

import cv2
import face_recognition
import numpy as np

from ai.face.face import Face

log = logging.getLogger(__name__)


def get_faces(rgb_frame):
    if rgb_frame is None:
        return None

    # Find the faces. Note the rgb format
    face_locations = face_recognition.face_locations(rgb_frame)
    if face_locations is None and len(face_locations) <= 0:
        return None

    # Return face list
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    face_landmarks = face_recognition.face_landmarks(rgb_frame, face_locations)

    faces = []
    for i, locations in enumerate(face_locations):
        face_img = get_face_img(rgb_frame, locations)
        faces.append(Face(i, locations, face_encodings[i], face_landmarks[i], face_img))

    return faces


def get_face_img(frame, locations, show_face=False):
    if frame is None or locations is None:
        return None

    top, right, bottom, left = locations
    height = bottom - top
    width = right - left

    face_img = np.zeros((height, width, 3), np.uint8)
    for i in range(height):
        for j in range(width):
            face_img[i][j] = frame[top + i][left + j]

    if show_face:
        cv2.imshow('Face', face_img)

    return face_img


def locate_faces(rgb_frame, known_faces, known_names, scale=1):
    if rgb_frame is None or len(known_faces) != len(known_names):
        return None, None

    # Scale frame for faster processing
    if scale > 1:
        scale_frame = cv2.resize(rgb_frame, (0, 0), fx=1.0 / scale, fy=1.0 / scale)
    else:
        scale_frame = rgb_frame

    # Find the faces. Note the rgb format
    face_locations = face_recognition.face_locations(scale_frame)
    face_encodings = face_recognition.face_encodings(scale_frame, face_locations)

    face_names = []
    for face_enc in face_encodings:
        # See if the face matches
        matches = face_recognition.compare_faces(known_faces, face_enc, tolerance=0.5)

        # If a match was found, just use the first one
        if True in matches:
            face_names.append(known_names[matches.index(True)])
        else:
            face_names.append(None)

    log.info('located faces: %s' % str(face_names))
    return face_locations, face_names


def mark_names(frame, face_locations, face_names, scale=1):
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
