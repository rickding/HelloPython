import jieba
import jieba.posseg as pseg

# 手动初始化，不调用时，使用延迟加载
jieba.initialize()

# 启动paddle模式
jieba.enable_paddle()

sentence = "丁献礼，西安交大硕士，系统分析师，资深架构。工作16年，全栈开发，带过20多人技术团队，担任过多个系统的技术负责人和架构师，擅长Java、Python，微服务，分布式，DevOps，云服务解决方案。"
print(sentence)

# 分词
answer = jieba.cut(sentence, use_paddle=True)
print("\npaddle模式下分词：", "/ ".join(answer))

# 其他模式分析，默认精确模式
print("\n全模式： ", "/ ".join(jieba.cut(sentence, cut_all=True)))
print("\n精确模式： ", "/ ".join(jieba.cut(sentence, cut_all=False)))
print("\n搜索引擎分词： ", ", ".join(jieba.cut_for_search(sentence)))

# 词性标注
words = []
for w, f in pseg.cut(sentence):
    words.append("[%s, %s]" % (w, f))

print("\n词性标注：", words)

words = []
for w, f in pseg.cut(sentence, use_paddle=True):
    words.append("[%s, %s]" % (w, f))

print("\npaddle模式下词性标注：", words)
