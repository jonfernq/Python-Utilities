import json

# Load the JSON data from file
with open('output.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Define the HTML template for the article
template = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <h1>{heading}</h1>
    <p>{date}</p>
    <p>Viewed: {viewed}</p>
    <div>{contents}</div>
</body>
</html>
'''

# Loop through the list of articles
for article in data:
    print('article: ', str(article))
    print('heading: ', str(article['heading'])) 
    # Extract the values from the dictionary
    filename = article['filename']
    heading = article['heading']
    date = article['date']
    viewed = article['viewed']
    contents = article['contents']

    # Create the HTML page using the template
    html = template.format(title=heading, heading=heading, date=date, viewed=viewed, contents=contents)

    # Write the HTML page to a file with the same name as the original file
    with open(filename, 'w', encoding='utf-8') as html_file:
        html_file.write(html)
