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

for hashtags in json_data['searchList']:
    tweet_data.update({hashtags: []})
    hashtagTweets = tweepy.Cursor(api.search, q=hashtags).items(50)

    for tweet in hashtagTweets:
        tweet_data[hashtags].append({
            "Created At": tweet.created_at.isoformat(' '),
            "Text": tweet.text
        })

with open('twitter-results.json', 'w') as fp:
    json.dump(tweet_data, fp, indent=2)
