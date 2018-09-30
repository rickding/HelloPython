import logging

import cv2
import face_recognition
from django.core.management.base import BaseCommand

from ai.decorator.run_time import run_time
from ai.face.change import ChangeFace
from ai.face.path_util import image_path
from ai.face.video_util import get_video_file
from ai.face.image_util import get_known_faces

log = logging.getLogger(__name__)


# https://github.com/ageitgey/face_recognition
class Command(BaseCommand):
    help = 'face in video'

    def handle(self, *args, **options):
        # Open the input video
        # video_input, video_len = get_video_capture()
        video_input, video_len = get_video_file('hamilton_clip.mp4')

        # Create an output file, note the resolution/frame rate matches input
        four_cc = cv2.VideoWriter_fourcc(*'XVID')
        video_output = cv2.VideoWriter(image_path('located.avi'), four_cc, 29.97, (640, 360))

        # Load faces
        known_names, known_faces = get_known_faces()

        # Change face
        change_face = ChangeFace()
        change_face.load_image_src(cv2.imread(image_path('obama.jpg')))

        face_locations = []
        face_names = []
        frame_number = 0
        while True:
            ret, frame = video_input.read()
            if not ret:
                break

            # Process
            frame_number += 1
            if frame_number % 4 == 1:
                face_locations, face_names = self.locate(frame, known_faces, known_names, 2)
            frame = self.mark(frame, face_locations, face_names, 2)

            # change_face.load_image_dst(frame)
            # frame = change_face.run()

            # Write image to output file
            log.info('Writing frame %d / %d, names: %s' % (frame_number, video_len, str(face_names)))
            video_output.write(frame)

            # Display the image
            cv2.imshow('Video', frame)

            # Quit by hitting 'q' or ESC on the keyboard
            if cv2.waitKey(1) & 0xFF in [ord('q'), 27]:
                break

        # Release handle
        video_output.release()
        video_input.release()
        cv2.destroyAllWindows()
        return 'frames: %d' % frame_number

    @run_time
    def locate(self, frame, known_faces, known_names, scale=4):
        if frame is None or len(known_faces) != len(known_names):
            return None, None

        # Scale frame for fast processing
        if scale > 1:
            scale_frame = cv2.resize(frame, (0, 0), fx=1.0 / scale, fy=1.0 / scale)
        else:
            scale_frame = frame

        # Convert BGR (openCV) to RGB (face_recognition)
        rgb_frame = scale_frame[:, :, ::-1]

        # Find the faces
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

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

    @run_time
    def mark(self, frame, face_locations, face_names, scale=4):
        if frame is None:
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
