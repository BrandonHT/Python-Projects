import PyPDF2
import sys

num_pdfs = len(sys.argv)-2
pdfs = sys.argv[1:len(sys.argv)-1]
print(pdfs)
output = sys.argv[len(sys.argv)-1]

def pdf_combiner(pdf_list, output):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write(output)

pdf_combiner(pdfs, output)