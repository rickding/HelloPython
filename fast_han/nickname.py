from fastHan import FastHan
import jieba.posseg as pseg
# import hanlp

model = FastHan()
# HanLP = hanlp.load(hanlp.pretrained.mtl.UD_ONTONOTES_TOK_POS_LEM_FEA_NER_SRL_DEP_SDP_CON_XLMR_BASE)

for sentence in ['上海后花园科技有限公司', '上海后花园传媒工作室', '后花园科技（上海）有限公司']:
    # FastHan中文分词
    print("\n", model(sentence, target="POS"))

    # jieba词性标注
    words = []
    for w, f in pseg.cut(sentence):
        words.append("[%s, %s]" % (w, f))

    print("\n", words)

    # HanLP中文分词
    # print(HanLP([sentence]))
