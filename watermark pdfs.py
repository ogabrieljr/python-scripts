import os

import PyPDF2

watermark = PyPDF2.PdfFileReader("watermark.pdf")
output = PyPDF2.PdfFileWriter()
merger = PyPDF2.PdfFileMerger()

if os.path.exists("output.pdf"):
    template = PyPDF2.PdfFileReader("output.pdf")
    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)
        output.write(open("watermarked.pdf", "wb"))

else:
    def pdf_combiner(pdf_list):
        for pdf in pdf_list:
            merger.append(pdf)
        merger.write("output.pdf")


    pdf_combiner(["pdf1.pdf", "pdf2.pdf"])
