使用tensorflow dlib opencv特定人脸识别
https://github.com/5455945/tensorflow_demo/tree/master/SpecificFaceRecognition

pip3 install tensorflow==1.2.1
pip3 install tensorflow_gpu==1.2.1
pip3 install numpy==1.13.1+mkl
pip3 install opencv-python==3.2.0
pip3 install dlib==19.4.0
# 一定要注意scikit-learn和scipy的版本
pip3 install scikit-learn==0.18.2
pip3 install scipy==0.19.1
# 该blog完整参考 http://tumumu.cn/2017/05/02/deep-learning-face/
# 源码地址:https://github.com/5455945/tensorflow_demo.git
# win10 Tensorflow_gpu1.2.1 python3.5.3 dlib opencv
# CUDA v8.0 cudnn-8.0-windows10-x64-v5.1
# 本实验需要有一个摄像头，笔记本自带的即可
# tensorflow_demo\SpecificFaceRecognition\get_my_faces.py 用dlib生成自己脸的jpg图像
# tensorflow_demo\SpecificFaceRecognition\get_my_faces_opencv.py 用opencv生成自己脸的jpg图像(效果没有dlib好)
# tensorflow_demo\SpecificFaceRecognition\set_other_faces.py 预处理lfw的人脸数据
# tensorflow_demo\SpecificFaceRecognition\train_faces.py 人脸识别训练
# tensorflow_demo\SpecificFaceRecognition\is_my_face.py 人脸识别测试
01 获取本人图片集 使用get_my_faces.py获取本人的10000张头像照片，保存到./my_faces目录。只需启动get_my_faces.py，坐在电脑前，摆出不同脸部表情和姿势即可。大约1小时左右可采集10000张。 get_my_faces_opencv.py是采用opencv库采集的，速度比dlib的get_my_faces.py快些。dlib效果会好些。

02 获取其他人脸图片集 下载 http://vis-www.cs.umass.edu/lfw/lfw.tgz 人脸数据集。 windows下，可以使用winrar解压，注意要先选[查看文件]，然后再解压，才能解压出所有子目录及文件。 加压后的文件放到./input_img目录下。 然后，使用set_other_people.py处理./input_img目录下的解压文件，把大约13000+张头像预处理到./other_faces目录。

03 训练模型 使用train_faces.py来训练模型，模型保持到./model目录下

04使用模型进行识别 使用is_my_face.py来验证模型，检测到是自己的脸时，返回true。