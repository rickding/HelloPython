import logging

import cv2
from django.core.management.base import BaseCommand

from ai.face.face_crop import CropFace
from ai.face.path_util import face_path
from ai.face.video_util import read_video

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'crop face in video'

    def handle(self, *args, **options):
        cropper = CropFace()

        # video
        video_input, video_len = read_video('hamilton_clip.mp4')

        frame_number = 0
        while True:
            ret, frame = video_input.read()
            if not ret:
                break

            frame_number += 1
            cv2.imshow('Video', frame)

            # Quit by hitting 'q' or ESC on the keyboard
            if cv2.waitKey(1) & 0xFF in [ord('q'), 27]:
                break

            # detect
            face_locations, faces = cropper.run(frame)
            log.info('faces: %d', len(faces))

            for i, face in enumerate(faces):
                cv2.imshow('Face', face)

                # 存在本地
                file_save = face_path('%d_%d.jpg' % (frame_number - 1, i))
                log.info('Face: %s', file_save)
                cv2.imwrite(file_save, face)

        cv2.destroyAllWindows()
        return str(frame_number)
