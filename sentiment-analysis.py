import json
import csv
import os

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


#TODO: make this function add analysis results to a csv file along with printing them
def print_result(annotations, searchTerm):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude
    resultPath = 'results/sentiment-scores/' + searchTerm

    if not os.path.exists(resultPath):
        os.makedirs(resultPath)

    if not os.path.exists(resultPath + '/analysisScores.csv'):
        open(resultPath + '/analysisScores.csv', 'w+')

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))

    with open(resultPath + '/analysisScores.csv', 'a') as csvfile:
        scoreWriter = csv.writer(
            csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        scoreWriter.writerow([score] + [magnitude])

    return 0


def analyze(tweet_text, searchTerm):
    client = language.LanguageServiceClient()

    document = types.Document(
        content=tweet_text,
        language='en',
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    # Print the results
    print_result(annotations, searchTerm)


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

            analyze(str(tweet['Text']), searchTerm)
            iterator += 1
