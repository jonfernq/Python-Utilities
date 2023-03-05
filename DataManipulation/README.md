## Data Manipulation

Also known as 'data wrangling' or 'data munging': "the process of cleaning, transforming, and preparing data for analysis."

"Data munging involves a variety of tasks such as handling missing data, 
converting data types, merging and joining datasets, filtering and sorting data, 
and creating new variables or features. It is an important step in the data analysis pipeline 
because raw data often contains errors, inconsistencies, and other issues that must be addressed 
before meaningful insights can be extracted."

### Repurposing Screen-Scraped Text 

Code for extracting info from a screen scraping of my published news articles into a repurposed portfolio:

- [walk.py](https://github.com/jonfernq/Python-Utilities/blob/main/DataManipulation/walk.py): walk directory tree, list files that exist. 
- [tree2folder.py](https://github.com/jonfernq/Python-Utilities/blob/main/DataManipulation/tree2folder.py): walk directory tree, copy files to a folder if they contain a string, namely my name 
- [extractinfo.py](https://github.com/jonfernq/Python-Utilities/blob/main/DataManipulation/extractinfo.py): Extract content and meta-data from screen-scraped article, rewrite as JSON.

- [json2html.py](https://github.com/jonfernq/Python-Utilities/blob/main/DataManipulation/json2html.py): Format articles stored as JSON into HTML articles. 
- [jsonextract.py](https://github.com/jonfernq/Python-Utilities/blob/main/DataManipulation/jsonextract.py): Extract the first n list items from JSON file, rewrite to new JSON file.  
- [mydata_first_50.json](https://github.com/jonfernq/Python-Utilities/blob/main/DataManipulation/mydata_first_50.json): JSON file of articles extracted from html screen scrape of articles. Then passed through jsonextract.py to make a reasonable sample to inspect (50 list items). 

- [tagswithclasses.py](https://github.com/jonfernq/Python-Utilities/blob/main/DataManipulation/tagswithclasses.py): Find all tags with classes in HTML page, to help understand structure or messy html tags.
- [tagextract.py](https://github.com/jonfernq/Python-Utilities/blob/main/DataManipulation/tagextract.py): Extract certain tags from html file to extract, re-organize and repurpose information in an HTML page. 
