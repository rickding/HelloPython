# coding: utf-8
import logging
import os

import cv2
import numpy as np
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
            rows, cols, channels = img.shape
            cropped = img[0:479, 0:cols]

            # 转换hsv
            hsv = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)

            # 图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
            thresh = cv2.inRange(hsv, np.array([90, 10, 125]), np.array([135, 180, 255]))
            erode = cv2.erode(thresh, None, iterations=2)
            dilate = cv2.dilate(erode, None, iterations=0)

            # 创建形状和尺寸的结构元素
            kernel = np.ones((3, 3), np.uint8)

            # 扩张待修复区域
            hi_mask = cv2.dilate(dilate, kernel, iterations=1)
            specular = cv2.inpaint(cropped, hi_mask, -5, flags=cv2.INPAINT_NS)

            # 合并
            htich = np.vstack((specular, img[479:rows, 0:cols]))

            # 保存图片
            cv2.imwrite("image/new_%s" % file, htich)

            '''
            blue=[]
            #获取mask,调整lower中h控制颜色
            lower_blue=np.array([90,10,125])
            upper_blue=np.array([135,180,255])
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            erode=cv2.erode(mask,None,iterations=1)
            dilate=cv2.dilate(erode,None,iterations=1)
            #腐蚀膨胀
            erode=cv2.erode(mask,None,iterations=1)
            cv2.imshow('erode',erode)
            dilate=cv2.dilate(erode,None,iterations=1)
            cv2.imshow('dilate',dilate)
            for i in range(rows):
                for j in range(cols):
                    if dilate[i,j]==255:
                        blue.append([i,j])
            for w in blue:
                x=w[0]
                y=w[1]
                img[x,y]=[255,255,255]
            '''

            '''
            cv2.imshow('Mask', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            '''
