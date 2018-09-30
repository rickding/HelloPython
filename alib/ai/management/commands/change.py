# -*- coding: utf-8 -*-
import logging

import cv2
from django.core.management.base import BaseCommand

from ai.face.change import ChangeFace
from ai.face.path_util import image_path

log = logging.getLogger(__name__)


# https://blog.csdn.net/hongbin_xu/article/details/79179194
class Command(BaseCommand):
    help = 'change face'

    def handle(self, *args, **options):
        changer = ChangeFace()
        changer.load_images(image_path('lin-manuel-miranda.png'), image_path('biden.jpg'))
        ret = changer.run(False, False)

        file_save = image_path('changed.jpg')
        cv2.imwrite(file_save, ret)
        return file_save
