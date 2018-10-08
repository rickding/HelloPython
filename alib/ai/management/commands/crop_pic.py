import logging

import cv2
import dlib
import numpy as np
from django.core.management.base import BaseCommand

from ai.face.path_util import model_path, image_path, face_path

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'crop face in pic'

    def handle(self, *args, **options):
        # dlib
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(model_path('shape_predictor_68_face_landmarks.dat'))

        # image
        frame = cv2.imread(image_path('obama_and_biden.jpg'))
        cv2.imshow('Pic', frame)

        # detect
        faces = detector(frame, 1)
        log.info('faces: %d', len(faces))

        for k, d in enumerate(faces):
            # 计算矩形大小
            # (x,y), (宽度width, 高度height)
            pos_start = tuple([d.left(), d.top()])
            pos_end = tuple([d.right(), d.bottom()])

            # 计算矩形框大小
            height = d.bottom() - d.top()
            width = d.right() - d.left()

            # 根据人脸大小生成空的图像
            img_blank = np.zeros((height, width, 3), np.uint8)

            for i in range(height):
                for j in range(width):
                    img_blank[i][j] = frame[d.top() + i][d.left() + j]

            cv2.imshow('face', img_blank)

            # 存在本地
            file_save = face_path('0_%d.jpg' % k)
            log.info('Face: %s', file_save)
            cv2.imwrite(file_save, img_blank)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return str(len(faces))
