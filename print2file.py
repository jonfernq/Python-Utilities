# print2file.py - 
# redirect print to a .txt file temporarily 

import sys

# Open a file for writing
with open('output.txt', 'w') as f:
    # Redirect standard output to the file
    sys.stdout = f

    # Now everything printed will be written to the file
    print('Hello, world!')
    print('This will also go to the file.')

    # Redirect standard output back to the console
    sys.stdout = sys.__stdout__
