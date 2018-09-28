# -*- coding: utf-8 -*-
import sys
import os
import dlib
import glob
import cv2

class face_clustering(object):
    def __init__(self, input_dir=None, output_dir=None, log = None):
        pwd = os.getcwd()# 获取当前路径
        model_path = os.path.join(pwd, 'model')
        self.shape_predictor_5_path = os.path.join(model_path, 'shape_predictor_5_face_landmarks.dat')
        self.shape_predictor_68_path = os.path.join(model_path, 'shape_predictor_68_face_landmarks.dat')
        self.face_recognizer_model_path = os.path.join(model_path, 'dlib_face_recognition_resnet_model_v1.dat')
        
        # 导入模型
        self.shape_predictor = dlib.shape_predictor(self.shape_predictor_68_path)
        self.detector = dlib.get_frontal_face_detector()
        self.face_recognizer = dlib.face_recognition_model_v1(self.face_recognizer_model_path)
        
        # 输入输出路径
        self.input_dir = input_dir
        self.output_dir = output_dir
        
        # 输出log信息，这里用的是textBrowser来输出log信息，所以传入的会是一个textBrowser实例
        self.log = log
        
        # 为后面操作方便，建了几个列表
#         self.descriptors = []
#         self.images = []
        
    def set_input_dir(self, input_dir):
        if input_dir is not None:
            self.input_dir = input_dir
    
    def set_output_dir(self, output_dir):
        if output_dir is not None:
            self.output_dir = output_dir
        
    def set_log(self, log):
        if log is not None:
            self.log = log
       
    # 解决OpenCV无法读取中文   
    def cv_imread(self, file_path = ""):
        file_path_gbk = file_path.encode('gbk')        # unicode转gbk，字符串变为字节数组
        img_mat = cv2.imread(file_path_gbk)  # 字节数组直接转字符串，不解码
        return img_mat 
    
    def run(self):
        if(os.path.exists(self.input_dir) == False):
            print(u'Input directory does not exist.Please check your input directory.')
            return
        if(self.output_dir is None):
            father_path = os.path.abspath(os.path.dirname(self.input_dir)+os.path.sep+".")
            self.output_dir = os.path.join(father_path, 'face_clustering_output')
            print(self.output_dir)
        # 为后面操作方便，建了几个列表
        descriptors = []
        images = []
        
        self.log.append(u'----'*30)# 分界符
        
        # 遍历faces文件夹中所有的图片
        for f in glob.glob(os.path.join(self.input_dir, "*.jpg")):
            print('Processing file：{}'.format(f))
            self.log.append(u'Processing file：{}'.format(f))
            # 读取图片
            img = self.cv_imread(f)
            # 转换到rgb颜色空间
            img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # 检测人脸
            dets = self.detector(img2, 1)
            print("Number of faces detected: {}".format(len(dets)))
            self.log.append(u"Number of faces detected: {}".format(len(dets)))
            # 遍历所有的人脸
            for index, face in enumerate(dets):
                # 检测人脸特征点
                shape = self.shape_predictor(img2, face)
                # 投影到128D
                face_descriptor = self.face_recognizer.compute_face_descriptor(img2, shape)
        
                # 保存相关信息
                descriptors.append(face_descriptor)
                images.append((img2, shape))
        
        self.log.append(u'----'*30)
        
        # 聚类
        labels = dlib.chinese_whispers_clustering(descriptors, 0.5)
        print("labels: {}".format(labels))
        self.log.append(u"labels: {}".format(labels))
        num_classes = len(set(labels))
        print("Number of clusters: {}".format(num_classes))
        self.log.append(u"Number of clusters: {}".format(num_classes))
        
        self.log.append(u'----'*30)
        
        # 为了方便操作，用字典类型保存
        face_dict = {}
        for i in range(num_classes):
            face_dict[i] = []
        # print face_dict
        for i in range(len(labels)):
            face_dict[labels[i]].append(images[i])
            
        
        # 遍历字典，保存结果
        for key in face_dict.keys():
            file_dir = os.path.join(self.output_dir, str(key))
            if not os.path.isdir(file_dir):
                os.makedirs(file_dir)
        
            for index, (image, shape) in enumerate(face_dict[key]):
                file_path = os.path.join(file_dir, 'face_' + str(index) + '.jpg')
                print file_path
#                 dlib.save_face_chip(image, shape, file_path, size=150, padding=0.25)
                res = dlib.get_face_chip(image, shape, size=150, padding=0.25)
                res = cv2.cvtColor(res, cv2.COLOR_RGB2BGR)
                cv2.imwrite(file_path, res)
        