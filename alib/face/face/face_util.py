import logging

import cv2
import face_recognition

log = logging.getLogger(__name__)


def recognize_faces(rgb_frame, known_faces, known_names, scale=1):
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
