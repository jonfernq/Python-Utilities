import os
import pytesseract
from PIL import Image

def ocr_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    summary_text = ''
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
            input_file_path = os.path.join(input_folder, file_name)
            output_file_path = os.path.join(output_folder, file_name.replace('.jpg', '.txt').replace('.jpeg', '.txt'))
            img = Image.open(input_file_path)
            text = pytesseract.image_to_string(img)
            summary_text += text + '\n'
            with open(output_file_path, 'w', encoding='utf-8') as fout:
                fout.write(text)
    with open(os.path.join(output_folder, 'summary.txt'), 'w', encoding='utf-8') as fout:
        fout.write(summary_text)

input_folder = "D:\\GITHUB_MY\\OCR\\INPUT"
output_folder = "D:\\GITHUB_MY\\OCR\\OUTPUT" 
ocr_folder(input_folder, output_folder)


