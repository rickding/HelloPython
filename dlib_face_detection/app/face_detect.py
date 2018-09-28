# -*- coding: utf-8 -*-
import sys 
import cv2
import dlib
import os

class face_detect(object):
    def __init__(self, img_path=None, method=0):
        pwd = os.getcwd()# 获取当前路径
        model_path = os.path.join(pwd, 'model')
        cnn_model_path = os.path.join(model_path, 'mmod_human_face_detector.dat')
        #print(cnn_model_path)
        self.detector = None
        if method == 0: # 采用默认模型
            self.detector = dlib.get_frontal_face_detector()
        elif method == 1:   # 采用CNN模型
            self.detector = dlib.cnn_face_detection_model_v1(cnn_model_path)
        else:
            pass
        self.method = method
        self.img_path = img_path
    
    def load_image(self, img_path):
        self.img_path = img_path
        
    # 解决OpenCV无法读取中文   
    def cv_imread(self, file_path = ""):
        file_path_gbk = file_path.encode('gbk')        # unicode转gbk，字符串变为字节数组
        img_mat = cv2.imread(file_path_gbk)  # 字节数组直接转字符串，不解码
        return img_mat 
    
    def run(self):
        if self.detector is None:
            print('No detector detected.Choose a correct one!')
            return
        if self.img_path is None:
            print('Image path is wrong.Please check it again!')
            return
        
#         img_bgr = cv2.imread(self.img_path, cv2.IMREAD_COLOR)
        img_bgr = self.cv_imread(self.img_path)
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        
        if self.method == 0: # 采用默认模型
            dets = self.detector(img_rgb, 1)
            print("Number of faces detected: {}".format(len(dets)))
            for index, face in enumerate(dets):
                print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(), face.bottom()))
                left = face.left()
                top = face.top()
                right = face.right()
                bottom = face.bottom()
                cv2.rectangle(img_rgb, (left, top), (right, bottom), (0, 255, 0), 3)
        elif self.method == 1:
            dets = self.detector(img_rgb, 1)
            print("Number of faces detected: {}".format(len(dets)))
            for i, d in enumerate(dets):
                face = d.rect
                print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(i, face.left(), face.top(), face.right(), d.rect.bottom(), d.confidence))
                left = face.left()
                top = face.top()
                right = face.right()
                bottom = face.bottom()
                cv2.rectangle(img_rgb, (left, top), (right, bottom), (0, 255, 0), 3)
        return img_rgb
            