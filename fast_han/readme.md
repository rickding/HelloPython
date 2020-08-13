# fastHan

## 运行环境
Ubuntu18.04, Python3.6

## 安装fastHan
pip3 install fastHan==1.3

- 注意依赖包：
torch>=1.0.0
fastNLP>=0.5.0

## 使用时只需两步：加载模型、输入句子。

from fastHan import FastHan

model = FastHan()

sentence = "复旦大学计算机教授，国产人工智能，汉语分析开源项目。";
print(sentence)

answer = model(sentence);
print(answer)

- 注意首次初始化模型时，将自动从服务器中下载模型数据，并且可以指定large版本，默认base。

model = FastHan(model_type="large")

- 模型分词时，可以指定target参数，可选"Parsing", "CWS", "POS", "NER"，默认CWS。

print(model(sentence, target="NER"))

## 常见问题
- 不能安装pip，首先运行update
sudo apt update
sudo apt install python3-pip

- 安装fastHan时，下载torch用时太长，建议使用阿里源
pip3 install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com fastHan==1.3
