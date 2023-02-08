# ocr.py - 
# produces .txt files from .jpg files with text 
# using Tesseract OCR library 

# https://linuxhint.com/install-tesseract-windows/ 
# https://builtin.com/data-science/python-ocr

from PIL import Image
import pytesseract
import numpy as np
 
def ocr_file(in_file, out_file):
    img1 = np.array(Image.open(in_file))
    text = pytesseract.image_to_string(img1)
    print(text) 
    with open(out_file, 'w', encoding='utf-8') as fout: 
        fout.write(text) 
    
in_file  = 'img_in.jpg'
out_file  = 'img_out.txt'
ocr_file(in_file, out_file) 

