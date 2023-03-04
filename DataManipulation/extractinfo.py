import os
import json
from bs4 import BeautifulSoup

# Define the directory to search for files in
# directory = '/path/to/directory'
directory = "D:\\GITHUB_MY\\BKPPORTFOLIO\\newfiles"  

# Create an empty list to store the dictionaries for each file
file_dicts = []

# Iterate over all the files in the directory
for filename in os.listdir(directory):
    # Skip directories
    if os.path.isdir(os.path.join(directory, filename)):
        continue

    # Create a dictionary for the file and add its filename
    file_dict = {'filename': filename}

    # Open the file
    with open(os.path.join(directory, filename), 'r', encoding='utf-8') as infile:
        # Read the contents of the file
        file_contents = infile.read()

        # Create a BeautifulSoup object from the file contents
        soup = BeautifulSoup(file_contents, 'html.parser')

        # Extract the heading
        heading_tag = soup.find('h1', {'itemprop': 'headline'})
        if heading_tag:
            file_dict['heading'] = heading_tag.text.strip()

        # Extract the date
        date_tag = soup.find('span', {'itemprop': 'datePublished'})
        if date_tag:
            file_dict['date'] = date_tag.text.strip()

        # Extract the viewed count
        view_tag = soup.find('span', {'class': 'view'})
        if view_tag:
            file_dict['viewed'] = view_tag.text.strip()

        # Extract the contents
        contents_tag = soup.find('div', {'class': 'articleContents'})
        if contents_tag:
            file_dict['contents'] = contents_tag.text.strip()

    # Add the dictionary to the list of dictionaries
    file_dicts.append(file_dict)

# Write the list of dictionaries to a JSON file
#with open('output.json', 'w', encoding='utf-8') as outfile:
#    json.dump(file_dicts, outfile)

with open('output.json', 'w', encoding='utf-8') as outfile:
    json.dump(file_dicts, outfile, ensure_ascii=False, indent=4) 
