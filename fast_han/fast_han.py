from fastHan import FastHan

model = FastHan()

sentence = "丁献礼，西安交大硕士，系统分析师，资深架构。工作16年，全栈开发，带过20多人技术团队，担任过多个系统的技术负责人和架构师，擅长Java、Python，微服务，分布式，DevOps，云服务解决方案。"
print(sentence)

answer = model(sentence);
print("\n默认CWS: ", answer)

# 模型分词时，可以指定target参数，可选"Parsing", "CWS", "POS", "NER"，默认CWS。
print("\nNER: ", model(sentence, target="NER"))
print("\nPOS: ", model(sentence, target="POS"))
print("\nParsing: ", model(sentence, target="Parsing"))
