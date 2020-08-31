from fastHan import FastHan

model = FastHan()

sentence = '''丁献礼
西安交大硕士，系统分析师，资深架构师
工作 16 年，全栈开发，带过 20 多人技术团队，担任过多个系统的技术负责人和架构师，擅长 Java、Python，
微服务，分布式，DevOps，云服务解决方案。
 权倾天下-开发嵌入式 IE 浏览器监控程序，《电脑爱好者》2004.10
 利用 Delphi7 开发数字水印管理系统，《电脑爱好者》2003.21
 基于内容的网络不良图像信息过滤系统的实现，《计算机与信息技术》2004.1
 基于 Delphi 的数据库复制程序，《计算机与信息技术》2003.1'''

print(sentence)

answer = model(sentence);
print("\n默认CWS: ", answer)

# 模型分词时，可以指定target参数，可选"Parsing", "CWS", "POS", "NER"，默认CWS。
print("\nNER: ", model(sentence, target="NER"))
print("\nPOS: ", model(sentence, target="POS"))
print("\nParsing: ", model(sentence, target="Parsing"))
