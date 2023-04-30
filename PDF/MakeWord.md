## Make Word File from Python

- Write a python function to create a new .docx file, insert a series of text messages, then insert all the .jpeg images in the a directory, then save the .docx file, and exit. 

Here's an example Python function that creates a new .docx file, inserts a series of text messages, and inserts all the .jpeg images in the specified directory:

```python

import os
from docx import Document
from docx.shared import Inches

def create_docx_with_images(docx_file_path, messages, images_dir):
    # Create an instance of a word document
    doc = Document()

    # Add messages to the document
    for message in messages:
        doc.add_paragraph(message)

    # Add all the images in the directory to the document
    for image_file in os.listdir(images_dir):
        if image_file.endswith(".jpeg"):
            image_path = os.path.join(images_dir, image_file)
            doc.add_picture(image_path, width=Inches(6))

    # Save the document to the specified file path
    doc.save(docx_file_path)

docx_file_path = "new_document.docx"
messages = ["Hello!", "This is a test.", "Here are some images:"]
images_dir = "D:\\github_my\\COBOL_learning\\heapsort"

create_docx_with_images(docx_file_path, messages, images_dir)
```
