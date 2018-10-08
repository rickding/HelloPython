import json
import logging

import cv2
from django.core.management.base import BaseCommand

from ai.face.face import FaceEncoder
from ai.face.face_util import get_faces
from ai.face.path_util import image_path, face_path, face_dir
from ai.util.file_util import save

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'profile face in pic'

    def handle(self, *args, **options):
        # image
        img_file = 'obama_and_biden'
        frame = cv2.imread(image_path('%s.jpg' % img_file))
        cv2.imshow('Pic', frame)

        # detect
        faces = get_faces(frame)
        log.info('faces: %d', len(faces))

        for i, face in enumerate(faces):
            cv2.imshow('Face', face.image)

            # 存在本地
            face.index = i
            face.image_file = '0_%d.jpg' % face.index
            file_save = face_path(face.image_file)
            log.info('Face: %s', file_save)
            cv2.imwrite(file_save, face.image)

        cv2.destroyAllWindows()

        if len(faces) <= 0:
            return 'No faces'

        profile = json.dumps(faces, cls=FaceEncoder)
        return save(face_dir(), '%s.json' % img_file, profile.encode('utf-8'))
