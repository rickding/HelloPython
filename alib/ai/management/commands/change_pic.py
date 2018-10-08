# -*- coding: utf-8 -*-
import logging

import cv2
from django.core.management.base import BaseCommand

from ai.face.face_change import ChangeFace
from ai.face.image_util import read_image
from ai.face.face_util import get_faces
from ai.face.path_util import image_path, output_path

log = logging.getLogger(__name__)


# https://blog.csdn.net/hongbin_xu/article/details/79179194
class Command(BaseCommand):
    help = 'change face in picture'

    def handle(self, *args, **options):
        changer = ChangeFace()
        file_save = None

        src_img_file = image_path('obama.jpg')
        dst_img_file = image_path('kit_with_rose.jpg')

        dst_img = read_image(dst_img_file)
        src_img = read_image(src_img_file)

        cv2.imshow('Pic Dst', dst_img)
        cv2.imshow('Pic Src', src_img)

        dst_faces = get_faces(dst_img)
        src_faces = get_faces(src_img)

        for i in range(0, len(dst_faces)):
            for j in range(0, len(src_faces)):
                changer.load_images(dst_img_file, src_img_file, index_1=i, index_2=j)
                img_changed = changer.run(False, False)

                file_save = output_path('changed_%d_%d.jpg' % (i, j))
                cv2.imwrite(file_save, img_changed)
                cv2.imshow('Changed Pic', read_image(file_save))

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return file_save
