## Data Manipulation

Also known as 'data wrangling' or 'data munging': "the process of cleaning, transforming, and preparing data for analysis."

"Data munging involves a variety of tasks such as handling missing data, 
converting data types, merging and joining datasets, filtering and sorting data, 
and creating new variables or features. It is an important step in the data analysis pipeline 
because raw data often contains errors, inconsistencies, and other issues that must be addressed 
before meaningful insights can be extracted."

### Repurposing Screen-Scraped Text 

Code for reformatting a screen scrape of my published news articles into a repurposed portfolio:

- [tree2folder.py](https://github.com/jonfernq/Python-Utilities/blob/main/DataManipulation/tree2folder.py): walk directory tree, copy files to a folder 
- [extractinfo.py](https://github.com/jonfernq/Python-Utilities/blob/main/DataManipulation/extractinfo.py): Extract content and meta-data from screen-scraped article, rewrite as JSON.
- [articles.json](https://github.com/jonfernq/Python-Utilities/blob/main/DataManipulation/articles.json): JSON file of articles extracted from html screen scrape of articles. 
- [json2html.py](https://github.com/jonfernq/Python-Utilities/blob/main/DataManipulation/json2html.py): Format articles stored as JSON into HTML articles. 
