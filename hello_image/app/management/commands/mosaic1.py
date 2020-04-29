# coding: utf-8
import logging

import cv2
import numpy as np
import os
from django.core.management.base import BaseCommand

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Hello Command'

    def handle(self, *args, **options):
        log.info("Hello Mosaic.")

        for file in os.listdir("image"):
            if file.startswith("new_"):
                continue

            path = "image/" + file
            img = cv2.imread(path)
            height, width, depth = img.shape[0:3]

            # 图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
            thresh = cv2.inRange(img, np.array([240, 240, 240]), np.array([255, 255, 255]))

            # 创建形状和尺寸的结构元素
            kernel = np.ones((3, 3), np.uint8)

            # 扩张待修复区域
            hi_mask = cv2.dilate(thresh, kernel, iterations=1)
            specular = cv2.inpaint(img, hi_mask, 5, flags=cv2.INPAINT_TELEA)

            # 保存图片
            cv2.imwrite("image/new_%s" % file, specular)

            # 显示
            cv2.namedWindow("Image", 0)
            cv2.resizeWindow("Image", int(width / 2), int(height / 2))
            cv2.imshow("Image", img)

            cv2.namedWindow("newImage", 0)
            cv2.resizeWindow("newImage", int(width / 2), int(height / 2))
            cv2.imshow("newImage", specular)

            cv2.waitKey(0)
            cv2.destroyAllWindows()
