from fastHan import FastHan

model = FastHan()

sentence = "复旦大学计算机教授，国产人工智能，汉语分析开源项目。";
print(sentence)

answer = model(sentence);
print(answer)


# 模型分词时，可以指定target参数，可选"Parsing", "CWS", "POS", "NER"，默认CWS。
print("\nNER: \n", model(sentence, target="NER"))
print("\nPOS: \n", model(sentence, target="POS"))
print("\nParsing: \n", model(sentence, target="Parsing"))
