
# ocr.py - 
# ocr  
# 
# install 
# https://linuxhint.com/install-tesseract-windows/ 
# https://builtin.com/data-science/python-ocr

from PIL import Image
import pytesseract
import numpy as np
import os  
import pathlib 

# make list of full paths of all images in 'from-directory'  
# iterate over this file list 
# convert each to text with ocr 
# write to 'to-directory'
# (Note: this is a repeated pattern
# so create a function to set-up and execute this iteration
# passing it an ocr function (strategy design pattern)  

def ocr_file(in_file, out_file):
    img1 = np.array(Image.open(in_file))
    text = pytesseract.image_to_string(img1)
    # print(text) 
    with open(out_file, 'w', encoding='utf-8') as fout: 
        fout.write(text) 
        
def change_filename(old_filename):
    stem = pathlib.Path(old_filename).stem 
    new_filename = 'raj' + stem[-4:] + '.txt'
    return new_filename  
    
base_dir = os.getcwd()
from_dir = base_dir + "\\from-directory"
to_dir = base_dir + "\\to-directory"
from_files = os.listdir(from_dir)
print(str(from_files)) 

for from_file in from_files:
    # print(from_file)
    to_file = change_filename(from_file)
    print(to_file)
    out_file = to_dir + "\\" + to_file
    in_image = from_dir + "\\" + from_file
    ocr_file(in_image, out_file)
quit()

in_file  = 'rajtst3.jpg'
out_file = 'text2.txt'
ocr_file(in_file, out_file)
quit() 

filename = 'rajtst3.jpg'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
print(text) 
with open('text2.txt', 'w', encoding='utf-8') as fout: 
    fout.write(text) 
