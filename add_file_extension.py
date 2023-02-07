# add_file_extension.py - 
# iterate over files in directory and sub-directory 
# adding a given file extension 

import os

def add_file_extension(dir_path, file_extension):
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if '.' not in filename or not filename.endswith(file_extension):
                new_file_path = file_path + file_extension
                os.rename(file_path, new_file_path)

if __name__ == '__main__':
    #dir_path = input('Enter directory path: ')
    #file_extension = input('Enter file extension to add: ')
    dir_path = "D:\\COBOL\\PROGRAMS\\Mainframe-master"
    file_extension = ".cbl" 
    add_file_extension(dir_path, file_extension)
