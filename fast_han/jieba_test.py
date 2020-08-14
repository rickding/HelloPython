import jieba
import jieba.posseg as pseg

# 启动paddle模式
jieba.enable_paddle()

sentence = "“结巴”中文分词，做最好的Python中文分词组件"
print(sentence)

# 分词
answer = jieba.cut(sentence, use_paddle=True)
print("\npaddle模式下分词：", "/ ".join(answer))

# 其他模式分析，默认精确模式
print("\n全模式： ", "/ ".join(jieba.cut(sentence, cut_all=True)))
print("\n精确模式： ", "/ ".join(jieba.cut(sentence, cut_all=False)))
print("\n搜索引擎分词： ", "/ ".join(jieba.cut_for_search(sentence)))


# 词性标注
print("\n词性标注：")
words = pseg.cut(sentence)
for w, f in words:
    print(w, f)

print("\npaddle模式下词性标注：")
for w, f in pseg.cut(sentence, use_paddle=True):
    print(w, f)
