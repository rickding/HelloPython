anacoda navigator 1.8.7
jupyter notebook 5.5.0

jupyter lab 0.34.3
spider 3.3.1

python 3.6

jupyter notebook
http://localhost:8888/lab

jupyter notebook --generate-config
C:\Users\username\.jupyter\jupyter_notebook_config
#c.NotebookApp.notebook_dir = ''


# https://conda.io/miniconda.html
conda install numpy


# pip
pip freeze > requirements.txt
pip install -r requirement.txt 


# https://blog.csdn.net/lsg_lsg_lsg/article/details/79036980
conda install -c menpo dlib


# https://www.cnblogs.com/AdaminXie/p/9032224.html
https://github.com/coneypo/Dlib_install.git
pip install dlib-19.7.0-cp36-cp36m-win_amd64.whl


#https://blog.csdn.net/hongbin_xu/article/details/76284134
git clone https://github.com/davisking/dlib.git

cd dlib
mkdir build
cd build
cmake .. -DDLIB_USE_CUDA=0 -DUSE_AVX_INSTRUCTIONS=1
cmake --build

cd ..
python3 setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA


Visual Studio 2017
CMake
