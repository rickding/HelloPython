import logging

import cv2
import dlib
import numpy as np

from ai.decorator.run_time import run_time

log = logging.getLogger(__name__)


class CropFace(object):
    def __init__(self):
        log.info('Starting CropFace...')

        # dlib
        self.detector = dlib.get_frontal_face_detector()

    @run_time
    def run(self, frame, show_faces=False):
        if frame is None:
            return None, None

        # detect
        face_locations = self.detector(frame, 1)
        log.info('faces: %d', len(face_locations))

        face_images = []
        for k, d in enumerate(face_locations):
            # 计算矩形大小
            # (x,y), (宽度width, 高度height)
            pos_start = tuple([d.left(), d.top()])
            pos_end = tuple([d.right(), d.bottom()])

            # 计算矩形框大小
            height = d.bottom() - d.top()
            width = d.right() - d.left()

            # 根据人脸大小生成空的图像
            face_img = np.zeros((height, width, 3), np.uint8)

            for i in range(height):
                for j in range(width):
                    face_img[i][j] = frame[d.top() + i][d.left() + j]

            face_images.append(face_img)
            if show_faces:
                cv2.imshow('Face', face_img)

        return face_locations, face_images
