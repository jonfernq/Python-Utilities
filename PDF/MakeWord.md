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
---
### Scaling Images 

Scale all images in one directory by 50% writing them to new directory.

```
import os
from PIL import Image

# Directory paths
from_dir = 'from-directory'
to_dir = 'to-directory'

# Create output directory if it doesn't exist
if not os.path.exists(to_dir):
    os.makedirs(to_dir)

# Iterate over files in from directory
for file_name in os.listdir(from_dir):
    if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
        # Open image file
        img_path = os.path.join(from_dir, file_name)
        with Image.open(img_path) as img:
            # Get new size
            width, height = img.size
            new_size = (int(width * 0.5), int(height * 0.5))

            # Scale image
            scaled_img = img.resize(new_size, resample=Image.BICUBIC)

            # Save scaled image to output directory
            out_path = os.path.join(to_dir, file_name)
            scaled_img.save(out_path)
```

---
### Scale Image (Another Version) 

> Write a python function to scale an image down by a certain percentage.  

Here's a Python function to scale an image down by a certain percentage using the Pillow library:

```python
from PIL import Image

def scale_image(image_path, scale_percent):
    # Open the image file
    image = Image.open(image_path)
    
    # Get the original size of the image
    width, height = image.size
    
    # Calculate the new dimensions
    new_width = int(width * scale_percent / 100)
    new_height = int(height * scale_percent / 100)
    
    # Scale down the image
    image = image.resize((new_width, new_height))
    
    # Return the scaled image object
    return image
```    
    
The scale_image function takes two arguments: the path to the image file and the percentage by which to scale the image. For example, if you want to scale the image down by 50%, you would pass in 50 as the scale_percent argument.

The function first opens the image file using the Pillow library's Image.open method. It then gets the original width and height of the image using the size attribute.

Next, the function calculates the new dimensions of the image based on the scale_percent argument. It then scales down the image using the resize method and returns the scaled image object.

You can use this function to scale down an image and then save the scaled image to a file using the save method of the Image object.

Then you can call the function and pass in the Document object, the image file path, and the scale percentage as parameters:

```python
doc = Document()
image_path = 'D:\\github_my\\COBOL_learning\\heapsort\\loop_2_end.jpeg'
scale_percent = 50
add_image(doc, image_path, scale_percent)
```

This code will scale the image down to 50% of its original size and add it to the document.

