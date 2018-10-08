import logging

import cv2

log = logging.getLogger(__name__)


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
