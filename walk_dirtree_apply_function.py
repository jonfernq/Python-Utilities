# walk_dirtree_apply_function.py -
# take a directory and apply a given function to every file name in the directory and subdirectories 

import os

def apply_func_to_files(dir_path, file_func):
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_func(filename)
            #new_filename = file_func(filename)
            #new_file_path = os.path.join(dirpath, new_filename)
            #os.rename(file_path, new_file_path)

if __name__ == '__main__':
    #dir_path = input('Enter directory path: ')
    dir_path = "D:\\COBOL\\PROGRAMS\\Mainframe-master"
    file_func = lambda x: print(x)   
    # file_func = lambda x: x.upper()
    apply_func_to_files(dir_path, file_func)

"""
Write a python program to take a directory and apply a given function to every file name in the directory and subdirectories ? 

In this code, apply_func_to_files takes in a directory path and a file function as inputs. It then walks the directory tree rooted at dir_path, applies the file function file_func to each file name, and renames the file with the new name returned by file_func.

In the example usage in __main__, the directory path D:\\COBOL\\PROGRAMS\\Mainframe-master and a file function lambda x: x.upper() that converts file names to uppercase are passed as inputs to apply_func_to_files.
"""
