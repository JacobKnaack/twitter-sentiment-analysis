import argparse
import json

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

twitter_results = json.load(open('./twitter-results.json'))

for hashtags in twitter_results:
    print (hashtags)

def print_results(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentence):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {} '.format(index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(score, magnitude))
    return 0

# TODO: This needs refactoring for tweet text not while text files
def analyze(twitter_text):
    client = language.LanguageServiceClient()

    with open(twitter_text, 'r') as tweet:
        content = tweet.read()

    document = type.Document(
        content = content,
        type = enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    print_result(annotations)

# TODO: analyze text from formatted document object containing all the twitter results

