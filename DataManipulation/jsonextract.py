import json
from itertools import islice

with open('mydata.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

first_50 = list(islice(data, 50))

with open('mydata_first_50.json', 'w', encoding='utf-8') as f:
    json.dump(first_50, f, ensure_ascii=False, indent=4)
