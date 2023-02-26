# strsubst11.py

"""
Function that reads in a file as a string, applies a series of string substitutions to it using regular expressions, and writes the modified string to a new file:
"""

import re

def string_substitution(input_file, output_file, substitutions):
    # Read in file as string
    with open(input_file, 'r') as f:
        text = f.read()
    
    # Apply substitutions to string using regex
    for pattern, repl in substitutions:
        text = re.sub(pattern, repl, text)
    
    # Write modified string to output file
    with open(output_file, 'w') as f:
        f.write(text)

# Define list of substitutions
#substitutions = [
#    (r'\bfoo\b', 'bar'),
#    (r'\baz\b', 'qux')
#]
substitutions = [
    (r"python\nCopy code", "\n```python"),
    (r"\na\)", "\n```\n\na)")
]

# Call string_substitution function
string_substitution('regular_expressions_questions.txt', 'output_file.txt', substitutions)
