# Python program to list out
# all the sub-directories and files
	

import os
	
# List to store all
# directories
L = []
	
# Traversing through Test
for root, dirs, files in os.walk('learning', topdown=True):  # os.walk('.', topdown=True) 
	
	# Adding the empty directory to
	# list
    if files: 
	    L.append((root, dirs, files))

print("List of all sub-directories and files:")
for i in L:
	print(i)
