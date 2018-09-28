# -*- coding: utf-8 -*-
import sys 
import cv2
import dlib
import os
import numpy as np

class face_align(object):
    def __init__(self, img_path=None):
        pwd = os.getcwd()# 获取当前路径
        model_path = os.path.join(pwd, 'model')
        # self.shape_predictor_5_path = os.path.join(model_path, 'shape_predictor_5_face_landmarks.dat')
        self.shape_predictor_68_path = os.path.join(model_path, 'shape_predictor_68_face_landmarks.dat')
        self.shape_predictor = dlib.shape_predictor(self.shape_predictor_68_path)
        self.detector = dlib.get_frontal_face_detector()
        
        self.img_path = img_path
        
    def load_image(self, img_path):
        self.img_path = img_path
        
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
        
        img_bgr = self.cv_imread(self.img_path)
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        
        dets = self.detector(img_rgb, 1) #使用detector进行人脸检测 dets为返回的结果
        # 检测到的人脸数量
        num_faces = len(dets)
#         print(num_faces)
        if num_faces == 0:
            print("Sorry, there were no faces found in '{}'".format(self.img_path))
            return
        elif num_faces != 1:
            print("Sorry, there were too many faces found in '{}'".format(self.img_path))
            return
            
        # 识别人脸特征点，并保存下来
        face = dlib.full_object_detections()
        for det in dets:
            face.append(self.shape_predictor(img_rgb, det))
            
        # 人脸对齐
        res_image = dlib.get_face_chips(img_rgb, face, size=320)
        res_image = np.array(res_image).astype(np.uint8)[0, :, :, :]#[1, 320, 320, 3]：第一维不需要，表示的是人脸数
#         print(res_image.shape)
        res_image = cv2.cvtColor(res_image, cv2.COLOR_RGB2BGR)# opencv下颜色空间为bgr，所以从rgb转换为bgr
#         cv2.imshow('result', res_image)
                
        return res_image