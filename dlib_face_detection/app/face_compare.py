# -*- coding: utf-8 -*-
import sys 
import cv2
import dlib
import os
# from dlib.examples.face_clustering import face_descriptor
import numpy as np

class face_compare(object):
    def __init__(self):
        pwd = os.getcwd()# 获取当前路径
        model_path = os.path.join(pwd, 'model')
        self.shape_predictor_path = os.path.join(model_path, 'shape_predictor_68_face_landmarks.dat')
        self.face_rec_model_path = os.path.join(model_path, 'dlib_face_recognition_resnet_model_v1.dat')

        # 读入模型
        self.detector = dlib.get_frontal_face_detector()
        self.shape_predictor = dlib.shape_predictor(self.shape_predictor_path)
        self.face_rec_model = dlib.face_recognition_model_v1(self.face_rec_model_path)
        
#         self.img_path = None
        self.template_list = None
        
        self.template_face_descriptor = []
        self.template_name = []
        
#     def load_image(self, img_path):
#         self.img_path = img_path
        
    def load_template(self, template_list):
        self.template_list = template_list
    
    # 解决OpenCV无法读取中文   
    def cv_imread(self, file_path = ""):
        file_path_gbk = file_path.encode('gbk')        # unicode转gbk，字符串变为字节数组
        img_mat = cv2.imread(file_path_gbk)  # 字节数组直接转字符串，不解码
        return img_mat 
    
    def create128DVector(self, img_path):
#         img_bgr = cv2.imread(img_path)
        img_bgr = self.cv_imread(img_path)
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        dets = self.detector(img_rgb, 1)# 检测人脸
        face_descriptor_list = []
        print("Number of faces detected: {}".format(len(dets)))
        for index, face in enumerate(dets):
            print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(), face.bottom()))
            
            shape = self.shape_predictor(img_rgb, face)
            face_descriptor = self.face_rec_model.compute_face_descriptor(img_rgb, shape)
            
            face_descriptor_list.append(face_descriptor)
            
        return face_descriptor
    
    def create_template(self):
        self.template_face_descriptor = []
        self.template_name = []
        for template_path in self.template_list:
            print(template_path)
            template_path = unicode(template_path)
            face_descriptor = self.create128DVector(template_path)
            self.template_face_descriptor.append(face_descriptor)
            
            name = template_path.strip().split('.')[0].split('\\')[-1]
            self.template_name.append(name)
            print(name)
            
    def isTheSamePerson(self, data1, data2):
        diff = 0
        # for v1, v2 in data1, data2:
            # diff += (v1 - v2)**2
#         print(data1)
        for i in xrange(len(data1)):
            diff += (data1[i] - data2[i])**2
        diff = np.sqrt(diff)
        print diff
        if(diff < 0.6):
            print "It's the same person"
            return True
        else:
            print "It's not the same person"
            return False
        
    def compareAgainstTemplate(self, img_path):
        if img_path == None:
            print('Please input a path')
            return
        if len(self.template_name) == 0:
            print('You have not created your template yet.')
            return
        
        unknownPersonData = self.create128DVector(img_path)
        res_list = []
        for index in range(len(self.template_name)):
            name = unicode(self.template_name[index])
            data = self.template_face_descriptor[index]
            print(u'Is %s'%name)
            res = self.isTheSamePerson(unknownPersonData, data)
            res_list.append(res)
        return res_list
            