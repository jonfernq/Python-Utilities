# long_line_paragraphs.py

# Takes a .txt file as an argument and reformats the paragraphs so that they are one long line of text without single line breaks:

# usage: 
# python reformat_text.py mytextfile.txt

import sys

# check if the filename is provided as an argument
if len(sys.argv) != 2:
    print("Please provide a filename as an argument")
    sys.exit(1)

# open the file and read its contents
with open(sys.argv[1], "r", encoding='utf-8') as f:
    contents = f.read()

# replace all occurrences of two line breaks with a space
contents = contents.replace("\n\n", "@@")

# replace all remaining line breaks with nothing
contents = contents.replace("\n", "")

# reverse
contents = contents.replace("@@","\n\n")

# print the reformatted text
sys.stdout = open('out.txt', 'w', encoding='utf-8') 
print(contents)
