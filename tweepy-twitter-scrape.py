import tweepy
import json
from tweepy import OAuthHandler

API_CONFIG = json.load(open('./.config.json'))

consumer_key = API_CONFIG["API_KEY"]
consumer_secret = API_CONFIG["API_SECRET"]
access_token = API_CONFIG["ACCESS_TOKEN"]
access_secret = API_CONFIG["ACCESS_TOKEN_SECRET"]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

json_data=json.load(open('./hashtags.json'))
tweet_data = {}

for searchTerms in json_data['searchList']:
    tweet_data.update({searchTerms: []})
    tweets = tweepy.Cursor(api.search, q=searchTerms, lang='en').items(100)

    for tweet in tweets:
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
           tweet_data[searchTerms].append({
                "Created At": tweet.created_at.isoformat(' '),
                "Text": tweet.text
            })

with open('results/twitter-raw-scrape.json', 'w') as fp:
    json.dump(tweet_data, fp, indent=2)

print ('twitter results generated')
