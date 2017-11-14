# twitter-sentiment-analysis

## Scrapes twitter for tweets and provides sentiment analysis with googles natural language API

### 11/14/2017

This is the beginning of this project. Currently the only useful module is the tweepy-twitter-scrapper

#### Fetching tweets by hashtag:
In order to grab tweets two things are required for the scrapper
* the hashtags.json file must contain hashtags to search format
* a .config.json file must be created containing an object with 4 key values:
```
{
  "API_KEY": "your-api-key-here",
  "API_SECRET": "your-api-secret-here",
  "ACCESS_TOKEN": "your-access-token-here",
  "ACCESS_TOKEN_SECRET": "your-access-token-here"
}
```

Once this is set you can scrap twitter for your tweets which will populate in a twitter-results json file.
