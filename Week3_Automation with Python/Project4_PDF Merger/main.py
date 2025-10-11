import PyPDF2
import os

#List of PDFs to merge
pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf']

merger = PyPDF2.PdfMerger()


for pdf in pdfs:
    if os.path.exists(pdf):
        merger.append(pdf)
        print(f"Added: {pdf}")
    else:
        print(f"Warning: {pdf} not found and will be skipped.")
# Replace with your PDF file names
merger.write("merged_output.pdf")
merger.close()
