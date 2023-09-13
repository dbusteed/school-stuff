# libs
import json
import re

# text files to convert
files = ['../data/ENGLAND.txt', '../data/AMERICA.txt']

lines = []

# for each file 
for f in files:
    
    # open it up
    for line in open(f, 'r', encoding='utf8'):
    
        try:
            # add each line seperated by comma 
            lines.append( re.sub(r'\n', '', line).split(',') )
        except:
            pass
        
# row[0] is the country label
# row[1] is the text of the tweet
output = {
    'country': [row[0] for row in lines], 
    'raw_text': [row[1] for row in lines]
}

# save `output` dictionary to a JSON file
with open('../data/country_tweets2.json', 'w', encoding='utf8') as f:
    f.write( json.dumps(output) )