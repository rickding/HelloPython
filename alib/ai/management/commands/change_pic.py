# -*- coding: utf-8 -*-
import logging

import cv2
from django.core.management.base import BaseCommand

from ai.face.change_face import ChangeFace
from ai.face.path_util import image_path, output_path

log = logging.getLogger(__name__)


# https://blog.csdn.net/hongbin_xu/article/details/79179194
class Command(BaseCommand):
    help = 'change face in picture'

    def handle(self, *args, **options):
        changer = ChangeFace()
        changer.load_images(image_path('lin-manuel-miranda.png'), image_path('biden.jpg'))
        ret = changer.run(False, False)

        file_save = output_path('changed.jpg')
        cv2.imwrite(file_save, ret)
        return file_save
