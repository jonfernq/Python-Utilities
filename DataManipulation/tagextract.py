from bs4 import BeautifulSoup
import sys 

# Set the path to the HTML file
# html_file = 'path/to/file.html'
html_file = "D:\\GITHUB_MY\\BKPPORTFOLIO\\found\\beggar-from-china-makes-good-money-in-thailand.html"

# Read the HTML file and parse it using Beautiful Soup
with open(html_file, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find the article tag with class="learning-article"
article_tag = soup.find('article', {'class': 'learning-article'})

# Extract the header tag inside the article tag
header_tag = article_tag.find('header')

# Extract the div tag with class="articleContents"
div_tag = soup.find('div', {'class': 'articleContents'})

# Extract the div tag with class="vocabularies"
vocabularies_tag = soup.find('div', {'class': 'vocabularies'})

sys.stdout = open('htmlextract.html', 'w', encoding='utf-8')   
# Print the contents of the tags
print(str(header_tag))
print(str(div_tag))
print(str(vocabularies_tag))

