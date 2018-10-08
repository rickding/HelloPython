import logging

import cv2
from django.core.management.base import BaseCommand

from ai.face.face_util import get_faces
from ai.face.path_util import image_path, face_path

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'profile face in pic'

    def handle(self, *args, **options):
        # image
        frame = cv2.imread(image_path('obama_and_biden.jpg'))
        cv2.imshow('Pic', frame)

        # detect
        faces = get_faces(frame)
        log.info('faces: %d', len(faces))

        for face in faces:
            cv2.imshow('Face', face.image)

            # 存在本地
            file_save = face_path('0_%d.jpg' % face.index)
            log.info('Face: %s', file_save)
            cv2.imwrite(file_save, face.image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return str(len(faces))
