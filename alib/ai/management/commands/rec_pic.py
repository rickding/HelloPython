# -*- coding: utf-8 -*-
import logging

import face_recognition
from django.core.management.base import BaseCommand

from ai.face.image_util import get_known_faces
from ai.face.path_util import image_path

log = logging.getLogger(__name__)


# https://blog.csdn.net/hongbin_xu/article/details/76284134
class Command(BaseCommand):
    help = 'face in picture'

    def handle(self, *args, **options):
        known_names, known_faces = get_known_faces()

        img_unknown = face_recognition.load_image_file(image_path('obama_and_biden.jpg'))
        enc_unknown = face_recognition.face_encodings(img_unknown)[0]

        results = face_recognition.compare_faces(known_faces, enc_unknown)
        log.info('compare_faces: %s', str(results))

        ret_arr = []
        for i in range(0, len(results)):
            if results[i]:
                ret_arr.append(known_names[i])

        return str(ret_arr)
