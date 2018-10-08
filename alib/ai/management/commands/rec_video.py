import logging

import cv2
from django.core.management.base import BaseCommand

from ai.face.face_util import mark_names, recognize_faces
from ai.face.image_util import get_known_faces
from ai.face.video_util import read_video
from ai.util.path_util import output_path

log = logging.getLogger(__name__)


# https://github.com/ageitgey/face_recognition
class Command(BaseCommand):
    help = 'face in video'

    def handle(self, *args, **options):
        # Open the input video
        # video_input, video_len = video_capture()
        video_input, video_len = read_video('hamilton_clip.mp4')

        # Create an output file, note the resolution/frame rate matches input
        four_cc = cv2.VideoWriter_fourcc(*'XVID')
        video_output = cv2.VideoWriter(output_path('recognized.avi'), four_cc, 29.97, (640, 360))

        # Load faces
        known_names, known_faces = get_known_faces()

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
                # Convert BGR (openCV) to RGB (face_recognition)
                rgb_frame = frame[:, :, ::-1]

                face_locations, face_names = recognize_faces(rgb_frame, known_faces, known_names, 2)

            frame = mark_names(frame, face_locations, face_names, 2)

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
