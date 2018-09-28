# -*- coding: utf-8 -*-

import os
import sys
import glob
import dlib
import cv2
import chardet

class object_detector(object):
    def __init__(self, train_xml_path, log=None):
        # options用于设置训练的参数和模式
        self.options = dlib.simple_object_detector_training_options()
#         self.options.add_left_right_image_flips = True
#         self.options.C = 5
#         self.options.epsilon = 0.01
#         self.options.num_threads = 4
#         self.options.detection_window_size = 6400
#         self.options.be_verbose = True
        
        self.train_xml_path = train_xml_path
#         print(self.train_xml_path)
#         print(os.path.abspath(self.train_xml_path))
        father_path=os.path.abspath(os.path.dirname(self.train_xml_path)+os.path.sep+".")
        self.model_path = os.path.join(father_path, 'detector.svm')
        
        self.log = log# 打印输出的信息到窗口中，即textBrowser中
    
    def set_log(self, log):
        if log is not None:
            self.log = log
    
    # 用于修改训练xml文件的路径  
    def set_train_xml_path(self, train_xml_path):
        if train_xml_path is not None:
            self.train_xml_path = train_xml_path
            father_path=os.path.abspath(os.path.dirname(self.train_xml_path)+os.path.sep+".")
            self.model_path = os.path.join(father_path, 'detector.svm')
            
    # 用于修改训练的参数和模式      
#     def set_options(self, add_left_right_image_flips=True, C=5, num_threads=4, be_verbose=True):
#         self.options = dlib.simple_object_detector_training_options()
#         self.options.add_left_right_image_flips = add_left_right_image_flips
#         self.options.C = C
#         self.options.num_threads = num_threads
#         self.options.be_verbose = be_verbose
        
    # 打印当前options设置
    def print_options(self):
        print(u'add_left_right_image_flips:{}'.format(self.options.add_left_right_image_flips))
        print(u'be_verbose:{}'.format(self.options.be_verbose))
        print(u'C:{}'.format(self.options.C))
        print(u'detection_window_size:{}'.format(self.options.detection_window_size))
        print(u'epsilon:{}'.format(self.options.epsilon))
        print(u'num_threads:{}'.format(self.options.num_threads))
        
        if self.log:
            self.log.append(u'--'*30)
            self.log.append(u'SVM训练参数：')
            self.log.append(u'add_left_right_image_flips:{}'.format(self.options.add_left_right_image_flips))
            self.log.append(u'be_verbose:{}'.format(self.options.be_verbose))
            self.log.append(u'C:{}'.format(self.options.C))
            self.log.append(u'detection_window_size:{}'.format(self.options.detection_window_size))
            self.log.append(u'epsilon:{}'.format(self.options.epsilon))
            self.log.append(u'num_threads:{}'.format(self.options.num_threads))
            self.log.append(u'--'*30)
        
    def train(self):
        print("start training:")
        # 注：必须要将unicode转成普通字符串，否则dlib无法读取，这个编码上的bug也是坑了我两个小时
        train_xml_path = str(self.train_xml_path)
        model_path = str(self.model_path)
#         print(train_xml_path)
#         print(model_path)
#         print(chardet.detect(train_xml_path))
#         xml = 'F:\\Python\\Programs\\my_dlib_face_detection_application\\images\\test_object_detector\\cats_train\\cat.xml'
#         model = 'F:\\Python\\Programs\\my_dlib_face_detection_application\\images\\test_object_detector\\cats_train\\detector.svm'
#         print(xml)
#         print(model)
#         print(chardet.detect(xml))
        
        dlib.train_simple_object_detector(train_xml_path, model_path, self.options)
        
        print("Training accuracy: {}".format(dlib.test_simple_object_detector(train_xml_path, model_path)))
        print("The SVM model is saved in {0}".format(model_path))
        
        if self.log:
            self.log.append(u'--'*30)
            self.log.append("Training complete!")
            self.log.append("Training accuracy: {}".format(dlib.test_simple_object_detector(train_xml_path, model_path)))
            self.log.append("The SVM model is saved in {0}".format(model_path))
            self.log.append(u'--'*30)
            
    # 解决OpenCV无法读取中文   
    def cv_imread(self, file_path = ""):
        file_path_gbk = file_path.encode('gbk')        # unicode转gbk，字符串变为字节数组
        img_mat = cv2.imread(file_path_gbk)  # 字节数组直接转字符串，不解码
        return img_mat 
    
    def predict(self, model_path, img_path):
        if model_path == None:
            print(u'Current model is not accessable!')
            return
        if img_path == None:
            print(u'Current Path is not valid!')
            return
        
        detector = dlib.simple_object_detector(str(model_path))# dlib需要输入原始字符串，否则可能因为编码问题报错
        
        img_bgr = self.cv_imread(img_path)
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        dets = detector(img_rgb, 1)
        print("Number of objects detected: {}".format(len(dets)))
        for index, obj in enumerate(dets):
            print('obj {}; left {}; top {}; right {}; bottom {}'.format(index, obj.left(), obj.top(), obj.right(), obj.bottom()))
            left = obj.left()
            top = obj.top()
            right = obj.right()
            bottom = obj.bottom()
            cv2.rectangle(img_bgr, (left, top), (right, bottom), (0, 255, 0), 3)
            
        return img_bgr