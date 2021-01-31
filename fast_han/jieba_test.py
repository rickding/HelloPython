import jieba
import jieba.posseg as pseg

# 手动初始化，不调用时，使用延迟加载
jieba.initialize()

# 启动paddle模式
jieba.enable_paddle()

# sentence = '''丁献礼
# 西安交大硕士，系统分析师，资深架构师
# 工作 16 年，全栈开发，带过 20 多人技术团队，担任过多个系统的技术负责人和架构师，擅长 Java、Python，
# 微服务，分布式，DevOps，云服务解决方案。
#  权倾天下-开发嵌入式 IE 浏览器监控程序，《电脑爱好者》2004.10
#  利用 Delphi7 开发数字水印管理系统，《电脑爱好者》2003.21
#  基于内容的网络不良图像信息过滤系统的实现，《计算机与信息技术》2004.1
#  基于 Delphi 的数据库复制程序，《计算机与信息技术》2003.1'''

# sentence = '南京村村播科技有限公司'
# sentence = '上海鹰锐文化传媒工作室'
sentence = '传扬信息科技（上海）有限公司'
# sentence = '上海羚驾科技有限公司'

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
