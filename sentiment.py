from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

def polarity_strength(p):
    return 'strong' if abs(p) > 0.5 else 'weak'

def subjectivity_strength(s):
    return 'high' if s > 0.5 else 'low'

while True:
    text = input('Enter text to analyze: ')
    if len(text) > 0:
        print('Analyzing...')

        blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
        classification = blob.sentiment.classification
        polarity = {
            'val': blob.polarity, 
            'strength': polarity_strength(blob.polarity) 
        }
        subjectivity = {
            'val': blob.subjectivity,
            'strength': subjectivity_strength(blob.subjectivity)
        }

        print('Sentiment:    ' + classification)
        print('Polarity:     {:0.4f} ({})'.format(polarity['val'], polarity['strength']))
        print('Subjectivity: {:0.4f} ({})\n'.format(subjectivity['val'], subjectivity['strength']))
        