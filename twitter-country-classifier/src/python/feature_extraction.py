# libs
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SID
from emoji import UNICODE_EMOJI
import pandas as pd
import re

# read in the unprocessed tweets
df = pd.read_json('../data/country_tweets.json')

# number of @USERs
df['at_count'] = df['raw_text'].apply( lambda txt: len(re.findall(r'@\w+', txt)) )

# number of #s
df['hash_count'] = df['raw_text'].apply( lambda txt: len(re.findall(r'\#\w+', txt)) )

# number of emoji
df['emoji_count'] = df['raw_text'].apply( lambda txt: len([char for char in txt if char in UNICODE_EMOJI]) )

# has url?
df['has_url'] = df['raw_text'].apply( lambda txt: 1 if len(re.findall(r'https://.+', txt)) > 0 else 0 )

# get rid of @USER, #tags, emoji, big spaces, and URLs --> clean_text
df['clean_text'] = df['raw_text'].apply( lambda txt: re.sub(r'@\w+', '', txt) )
df['clean_text'] = df['clean_text'].apply( lambda txt: re.sub(r'\#\w+', '', txt) )
df['clean_text'] = df['clean_text'].apply( lambda txt: re.sub(r'https://.+', '', txt) )
df['clean_text'] = df['clean_text'].apply( lambda txt: ''.join([char for char in txt if char not in UNICODE_EMOJI]) )
df['clean_text'] = df['clean_text'].apply( lambda txt:  re.sub(r'\s{2}', ' ', txt) )

# number of characters
df['text_len'] = df['clean_text'].apply( lambda txt: len(txt) )

# number of words
df['word_count'] = df['clean_text'].apply( lambda txt: len(txt.split(' ')) )

# sentiment of tweet
sid = SID()
df['sentiment'] = df['clean_text'].apply( lambda txt: sid.polarity_scores(txt)['compound'] )

# df.head()
# df.describe()

# save to a new JSON file
df.to_json('../data/processed_tweets.json')