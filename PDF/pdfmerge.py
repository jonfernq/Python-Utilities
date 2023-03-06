# importing required modules
import PyPDF2, os

def list_pdf_files(directory):
    pdf_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            pdf_files.append(os.path.join(directory, filename))
    return pdf_files

def PDFmerge(pdfs, output):
	# creating pdf file merger object
	pdfMerger = PyPDF2.PdfMerger()

	# appending pdfs one by one
	for pdf in pdfs:
		pdfMerger.append(pdf)

	# writing combined pdf to output pdf file
	with open(output, 'wb') as f:
		pdfMerger.write(f)


def main():
	# pdf files to merge
	#pdfs = ['example.pdf', 'rotated_example.pdf']
	directory = 'socialcapital'
	pdfs = list_pdf_files(directory)

	# output pdf file name
	output = 'combined_example.pdf'

	# calling pdf merge function
	PDFmerge(pdfs=pdfs, output=output)


if __name__ == "__main__":
	# calling the main function
	main()
