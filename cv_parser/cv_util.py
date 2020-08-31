# -*- coding: utf-8 -*-
import io

import jieba
import jieba.posseg as pseg
from pdf_util import PDFUtil


class CVUtil:
    def __init__(self):
        pass

    @staticmethod
    def parse_cv(sentence, flag_list):
        # 手动初始化，不调用时，使用延迟加载
        jieba.initialize()

        # 启动paddle模式
        jieba.enable_paddle()

        # 词性标注
        content = {}
        cv = {}
        for w, f in pseg.cut(sentence, use_paddle=True):
            content[w] = f

            # 提取简历要素
            if f in flag_list:
                cv[w] = f

        print("\n词性标注：", content)
        return cv


if __name__ == '__main__':
    pdf_file = u'dingxl.pdf'
    cv_content = PDFUtil.pdf2txt(pdf_file)
    print("\n简历内容：", cv_content)

    cv_dict = CVUtil.parse_cv(cv_content, ["PER", "ORG", "nw"])
    print("\n解析要素：", cv_dict)
