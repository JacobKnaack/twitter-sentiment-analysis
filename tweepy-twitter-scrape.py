import tweepy
import json
import os
from tweepy import OAuthHandler

if os.environ["API_KEY"] is None:
    print ("Credentials not configured, please create a .env_config.sh file and export your API credentials.\n\n For help please visit https://github.com/JacobKnaack/twitter-sentiment-analysis")

consumer_key = os.environ["API_KEY"]
consumer_secret = os.environ["API_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_secret = os.environ["ACCESS_TOKEN_SECRET"]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

json_data=json.load(open('./hashtags.json'))
tweet_data = {}

for searchTerms in json_data['searchList']:
    tweet_data.update({searchTerms: []})
    tweets = tweepy.Cursor(api.search, q=searchTerms, lang='en').items(5)

    for tweet in tweets:
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
           tweet_data[searchTerms].append({
                "Created At": tweet.created_at.isoformat(' '),
                "Text": tweet.text
            })

if not os.path.exists('results/'):
    os.makedirs('results/')

with open('results/twitter-raw-scrape.json', 'w+') as fp:
    json.dump(tweet_data, fp, indent=2)

print ('twitter results generated')
