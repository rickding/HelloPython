# -*- coding: utf-8 -*-
import io

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser


class PDFUtil:
    def __init__(self):
        pass

    @staticmethod
    def pdf2txt(file_path):
        output = io.StringIO()

        with open(file_path, 'rb') as f:
            parser = PDFParser(f)
            doc = PDFDocument(parser)

            if not doc.is_extractable:
                raise PDFTextExtractionNotAllowed

            resource = PDFResourceManager()
            params = LAParams()
            device = PDFPageAggregator(resource, laparams=params)
            interpreter = PDFPageInterpreter(resource, device)

            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
                layout = device.get_result()
                for x in layout:
                    if hasattr(x, "get_text"):
                        content = x.get_text()
                        output.write(content)

        content = output.getvalue()
        output.close()

        return content


if __name__ == '__main__':
    print(PDFUtil.pdf2txt(u'dingxl.pdf'))
