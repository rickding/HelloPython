# -*- coding: utf-8 -*-

import os
import dlib
import cv2

class shape_predictor(object):
    def __init__(self, train_xml_path, log=None):
        self.options = dlib.shape_predictor_training_options()
        
        self.train_xml_path = train_xml_path
        father_path=os.path.abspath(os.path.dirname(self.train_xml_path)+os.path.sep+".")
        self.model_path = os.path.join(father_path, 'predictor.dat')
        
        self.log = log# 打印输出的信息到窗口中，即textBrowser中
        
    # 用于修改训练xml文件的路径  
    def set_train_xml_path(self, train_xml_path):
        if train_xml_path is not None:
            self.train_xml_path = train_xml_path
            father_path=os.path.abspath(os.path.dirname(self.train_xml_path)+os.path.sep+".")
            self.model_path = os.path.join(father_path, 'predictor.dat')
            
    def set_log(self, log):
        if log is not None:
            self.log = log
    
    # be_verbose:False
    # cascade_depth:10
    # feature_pool_region_padding:0.0
    # feature_pool_size:400
    # lambda_param:0.1
    # nu:0.1
    # num_test_splits:20
    # num_trees_per_cascade_level:500
    # oversampling_amount:20
    # random_seed:
    # tree_depth:4
    def print_options(self):
        print(u'参数：')
        print(u'be_verbose:{0}'.format(self.options.be_verbose))
        print(u'cascade_depth:{0}'.format(self.options.cascade_depth))
        print(u'feature_pool_region_padding:{0}'.format(self.options.feature_pool_region_padding))
        print(u'feature_pool_size:{0}'.format(self.options.feature_pool_size))
        print(u'lambda_param:{0}'.format(self.options.lambda_param))
        print(u'nu:{0}'.format(self.options.nu))
        print(u'num_test_splits:{0}'.format(self.options.num_test_splits))
        print(u'num_trees_per_cascade_level:{0}'.format(self.options.num_trees_per_cascade_level))
        print(u'oversampling_amount:{0}'.format(self.options.oversampling_amount))
#         print(u'random_seed:{0}'.format(self.options.random_seed))
        print(u'tree_depth:{0}'.format(self.options.tree_depth))
        
        if self.log is not None:
            self.log.append(u'--'*30)
            self.log.append(u'参数：')
            self.log.append(u'be_verbose:{0}'.format(self.options.be_verbose))
            self.log.append(u'cascade_depth:{0}'.format(self.options.cascade_depth))
            self.log.append(u'feature_pool_region_padding:{0}'.format(self.options.feature_pool_region_padding))
            self.log.append(u'lambda_param:{0}'.format(self.options.lambda_param))
            self.log.append(u'nu:{0}'.format(self.options.nu))
            self.log.append(u'num_test_splits:{0}'.format(self.options.num_test_splits))
            self.log.append(u'num_trees_per_cascade_level:{0}'.format(self.options.num_trees_per_cascade_level))
            self.log.append(u'oversampling_amount:{0}'.format(self.options.oversampling_amount))
            self.log.append(u'tree_depth:{0}'.format(self.options.tree_depth))
            self.log.append(u'--'*30)
            
    def train(self):
        # 调用dlib的函数之前先要把字符串转成普通字符串，否则可能由于编码问题报错
        xml_path = str(self.train_xml_path)
        model_path = str(self.model_path)
        print(xml_path)
        print(model_path)
        dlib.train_shape_predictor(xml_path, model_path, self.options)
        # 打印在训练集中的准确率
        print "\nTraining accuracy:{0}".format(dlib.test_shape_predictor(xml_path, model_path))
        if self.log:
            self.log.append(u'--'*30)
            self.log.append(u'Training complete!')
            self.log.append(u"\nTraining accuracy:{0}".format(dlib.test_shape_predictor(xml_path, model_path)))
            self.log.append(u'model saved in {0}'.format(self.model_path))
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
        
        # 导入训练好的模型文件
        predictor = dlib.shape_predictor(model_path)

        detector = dlib.get_frontal_face_detector()
        
        img_bgr = self.cv_imread(img_path)
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        dets = detector(img_rgb, 1)
        print("Number of faces detected: {}".format(len(dets)))
        for index, face in enumerate(dets):
            print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(), face.bottom()))
            shape = predictor(img_rgb, face)
            
            for index, pt in enumerate(shape.parts()):
                print('Part {}: {}'.format(index, pt))
                pt_pos = (pt.x, pt.y)
                cv2.circle(img_bgr, pt_pos, 2, (255, 0, 0), 1)
        
        return img_bgr
    