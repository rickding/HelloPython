import logging

import cv2
from django.core.management.base import BaseCommand

from ai.face.face_change import ChangeFace, NoFace, WrongFaceIndex
from ai.face.video_util import read_video
from ai.util.path_util import output_path

log = logging.getLogger(__name__)


# Change face in dst, replaced by the one from src
class Command(BaseCommand):
    help = 'change face in video'

    def handle(self, *args, **options):
        # Open the input video
        # video_input, video_len = video_capture()
        video_dst, video_len_dst = read_video('short_hamilton_clip.mp4')
        video_src, video_len_src = read_video('dingxl.mp4')
        video_len = min(video_len_dst, video_len_src)
        log.info('Dst: %d, src: %d' % (video_len_dst, video_len_src))

        # Create an output file, note the resolution/frame rate matches input
        four_cc = cv2.VideoWriter_fourcc(*'XVID')
        video_output = cv2.VideoWriter(output_path('changed.avi'), four_cc, 29.97, (640, 360))

        # Change face
        change_face = ChangeFace()

        frame_number = 0
        while True:
            ret, frame_dst = video_dst.read()
            if not ret:
                break

            ret, frame_src = video_src.read()
            if not ret:
                break

            # Display the image
            cv2.imshow('Video Dst', frame_dst)
            cv2.imshow('Video Src', frame_src)

            # Process
            frame_number += 1
            log.info('Process frame %d / %d' % (frame_number, video_len))

            try:
                cv2.imwrite(output_path('frame_dst.jpg'), frame_dst)
                change_face.load_image_dst(cv2.imread(output_path('frame_dst.jpg')))

                cv2.imwrite(output_path('frame_src.jpg'), frame_src)
                change_face.load_image_src(cv2.imread(output_path('frame_src.jpg')))

                frame_changed = change_face.run()

                cv2.imwrite(output_path('changed.jpg'), frame_changed)
                frame_changed = cv2.imread(output_path('changed.jpg'))
            except (NoFace, WrongFaceIndex) as e:
                log.error('Error when change_face: %s' % str(e))
                frame_changed = frame_dst

            # Write image to output file
            cv2.imshow("Changed Video", frame_changed)
            video_output.write(frame_changed)

            # Quit by hitting 'q' or ESC on the keyboard
            if cv2.waitKey(1) & 0xFF in [ord('q'), 27]:
                break

        # Release handle
        video_output.release()
        video_dst.release()
        video_src.release()

        cv2.destroyAllWindows()
        return 'frames: %d' % frame_number
