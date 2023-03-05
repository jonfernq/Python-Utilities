from bs4 import BeautifulSoup
import sys 

# Set the path to the HTML file
# html_file = 'path/to/file.html'
html_file = "D:\\GITHUB_MY\\BKPPORTFOLIO\\found\\beggar-from-china-makes-good-money-in-thailand.html"

# Read the HTML file and parse it using Beautiful Soup
with open(html_file, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find all tags with CSS classes
tags_with_classes = soup.find_all(class_=True)

sys.stdout = open('divspan.txt', 'w', encoding='utf-8')   
# Print the tags and their CSS classes
for tag in tags_with_classes:
    print(tag.name, tag.get('class'))
