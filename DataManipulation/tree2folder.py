# tree2folder.py - 
# walk directory tree, copy files to a folder 

import os
import shutil

# Define the root directory to start the search from
root_dir = "D:\\GITHUB_MY\\BKPPORTFOLIO\\learning"  

# Define the name of the output directory
output_dir = 'found'

# Define the search string
search_string = 'Fernquest'

# Define the path to the output directory
output_path = os.path.join(root_dir, output_dir)

# Create the output directory if it doesn't exist
if not os.path.exists(output_path):
    os.mkdir(output_path)

# Traverse the directory tree starting from the root directory
for dirpath, dirnames, filenames in os.walk(root_dir):
    #print(filenames) 
    # Iterate over the files in the current directory
    for file in filenames:
        # Create the full path to the file
        file_path = os.path.join(dirpath, file)
        # Open the file for reading
        #print(file_path) 
        with open(file_path, 'r', encoding='utf-8') as infile: 
            # Read the contents of the file
            #file_contents = infile.read()
            
            try:
                file_contents = infile.read()
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
                continue
            
            # Check if the search string is in the file
            if search_string in file_contents:
                # Create the path to the output file
                output_file_path = os.path.join(output_path, file)
                # Copy the file to the output directory
                shutil.copy2(file_path, output_file_path)
