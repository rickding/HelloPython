import logging

import cv2
from django.core.management.base import BaseCommand

from ai.face.face_util import profile_faces, save_profile
from ai.util.file_util import set_ext
from ai.util.path_util import image_path

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'profile face in pic'

    def handle(self, *args, **options):
        # image
        img_file = 'kit_with_rose.jpg'
        frame = cv2.imread(image_path(img_file))
        cv2.imshow('Pic', frame)

        # profile
        faces = profile_faces(frame)
        log.info('faces: %d', len(faces))

        cv2.destroyAllWindows()

        # save
        return save_profile(faces, set_ext(img_file, '.json'))
