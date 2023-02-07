# srclisitng.py - 
# for all files in a directory and its sub-directories
# copy into a file named: srclisting.txt 

import os

def copy_all_files(dir_path):
    with open('srclisting.txt', 'w', encoding='utf-8') as outfile:
        for dirpath, dirnames, filenames in os.walk(dir_path):
            for filename in filenames:
                print('filename: ', filename) 
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())

if __name__ == '__main__':
    #dir_path = input('Enter directory path: ')
    dir_path = "D:\\COBOL\\PROGRAMS\\Mainframe-master"
    copy_all_files(dir_path)
