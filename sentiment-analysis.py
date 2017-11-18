import json
import os

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


#TODO: make this function add analysis results to a csv file along with printing them
def print_results(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {} '.format(index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(score, magnitude))
    return 0


def analyze(twitter_text_file):
    client = language.LanguageServiceClient()

    with open(twitter_text_file, 'r') as tweet:
        content = tweet.read()

    document = types.Document(
        content = content,
        type = enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    print_results(annotations)


if __name__ == '__main__':
    twitter_data = json.load(open('results/twitter-raw-scrape.json'))

    for searchTerm in twitter_data:
        txtPath = 'results/twitter-text/' + searchTerm
        iterator = 0

        if not os.path.exists(txtPath):
            os.makedirs(txtPath)

        for tweet in twitter_data[searchTerm]:
            tweet_file = open(txtPath + '/tweet_' + str(iterator) + '.txt', 'w+')
            tweet_file.write(str(tweet['Text']))
        
            analyze(txtPath + '/tweet_' + str(iterator) + '.txt')
            iterator += 1
