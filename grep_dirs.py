# grep_dirs.py
# walks directories from root directory 
# reporting on matches to a string or regular expression
# defaults to current directory, if no directory given 
# a list of excluded extensions can be given
# only searches unicode texts, if not unicode and cannot open 
# file, indication is given in a message 

import sys
import os
import re
import mimetypes
from tabulate import tabulate

EXCLUDED_EXTENSIONS = ['.csv']

def grep(root_dir, search_string, regex=False):
    results = []

    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            file_ext = os.path.splitext(filename)[1]

            if file_ext in EXCLUDED_EXTENSIONS:
                continue

            mime_type = mimetypes.guess_type(filename)[0]
            if mime_type is None or not mime_type.startswith('text'):
                continue

            file_path = os.path.join(root, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_number, line in enumerate(f, start=1):
                        if regex:
                            if re.search(search_string, line):
                                results.append((file_path, line_number, line))
                        else:
                            if search_string in line:
                                results.append((file_path, line_number, line))
            except UnicodeDecodeError:
                results.append((file_path, 'Cannot read, non-unicode'))

    if results:
        print(tabulate(results, headers=['File', 'Line', 'Content']))

        with open('grep_results.txt', 'w', encoding='utf-8') as f:
            f.write(tabulate(results, headers=['File', 'Line', 'Content']))
    else:
        print('No results found')

if __name__ == '__main__':
    search_string = sys.argv[1]
    root_dir = '.'
    regex = False

    for i in range(2, len(sys.argv)):
        if sys.argv[i] == '-root':
            root_dir = sys.argv[i + 1]
        if sys.argv[i] == '-regex':
            regex = True

    grep(root_dir, search_string, regex)


"""

This code can be run from the command line as python grep.py [search_string] [-root [root_directory]] [-regex], where the -root and -regex arguments are optional.

It only requires the search string or regular expression as the first argument, and uses the current directory as the root directory if none is provided, and uses the -root and -regex arguments to specify the root directory and regular expression, respectively:

This code uses the mimetypes module to guess the MIME type of each file based on its extension, and skips over files whose MIME type doesn't start with text/. The code also opens all text files with the utf-8 encoding.

If the mimetypes module is unable to determine the MIME type of the file based on its extension. To handle this case, you can add a check for None before calling the startswith method

This code uses the tabulate library to nicely format the search results in a table, which is then written to a utf-8 encoded text file grep_results.txt. The code also includes a list EXCLUDED_EXTENSIONS of file extensions to skip over, including .csv.

In this code, we use a try-except block to catch the UnicodeDecodeError that might occur if a file can't be read as a utf-8 encoded text file. If an error occurs, a tuple containing the file path and an error message is added to the results list. The error message will be included in the output file along with the search results.


"""
