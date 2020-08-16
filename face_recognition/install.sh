#!/bin/bash
python3 -m pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --upgrade pip

# http://pypi.douban.com/simple
# http://mirrors.aliyun.com/pypi/simple/
pip3 install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirements.txt
