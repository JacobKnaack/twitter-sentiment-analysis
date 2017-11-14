import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def print_results(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annomatinos.sentence):
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
        content = content
        type = enums.Document.type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    print_result(annotations)

# TODO: this is for a file and I want for indivudal text object
if __name__ == '__main__':
    parser = argparser.ArgumentParser(
        description = __doc__
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'twitter_text',
        help = 'The you are analyzing this tweet')
