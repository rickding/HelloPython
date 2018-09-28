# -*- coding: utf-8 -*-
import sys 
import cv2
import dlib
import os

class face_landmark(object):
    def __init__(self, img_path=None, method=0):
        pwd = os.getcwd()# 获取当前路径
        model_path = os.path.join(pwd, 'model')
        self.shape_predictor_5_path = os.path.join(model_path, 'shape_predictor_5_face_landmarks.dat')
        self.shape_predictor_68_path = os.path.join(model_path, 'shape_predictor_68_face_landmarks.dat')
        self.shape_predictor = None
        self.detector = dlib.get_frontal_face_detector()
        
        self.load_method(method)    # 根据传入的参数选择使用的模型
        self.img_path = img_path
        
    def load_image(self, img_path):
        self.img_path = img_path
        
    def load_method(self, method=0):
        if method == 0:
            self.shape_predictor = dlib.shape_predictor(self.shape_predictor_5_path)
        elif method == 1:
            self.shape_predictor = dlib.shape_predictor(self.shape_predictor_68_path)
        else:
            self.shape_predictor = dlib.shape_predictor(self.shape_predictor_5_path)
        
    # 解决OpenCV无法读取中文   
    def cv_imread(self, file_path = ""):
        file_path_gbk = file_path.encode('gbk')        # unicode转gbk，字符串变为字节数组
        img_mat = cv2.imread(file_path_gbk)  # 字节数组直接转字符串，不解码
        return img_mat 
      
    def run(self):
        if self.shape_predictor is None:
            print(u'Error when loading the shape_detector!')
            return
        elif self.img_path is None:
            print(u'Image path is not valid!')
            return
        
#         img_bgr = cv2.imread(self.img_path)
        img_bgr = self.cv_imread(self.img_path)
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_RGB2BGR)
        
        dets = self.detector(img_rgb, 1) #使用detector进行人脸检测 dets为返回的结果
        print("Number of faces detected: {}".format(len(dets)))   # 打印识别到的人脸个数
        for index, face in enumerate(dets):
            print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(), face.bottom()))
            shape = self.shape_predictor(img_rgb, face)  # 寻找人脸的标定点
            for index, pt in enumerate(shape.parts()):
                print('Part {}: {}'.format(index, pt))
                pt_pos = (pt.x, pt.y)
                cv2.circle(img_rgb, pt_pos, 2, (255, 0, 0), 1)
                
        return img_rgb
                
            