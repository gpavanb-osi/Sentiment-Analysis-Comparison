import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class NLTKSentiment(object):

    def __init__(self):
        # No training here
        self.sid = SentimentIntensityAnalyzer()

    def sentiment(self, text):
        # Get list of sentences
        sentences = nltk.sent_tokenize(text)

        # Return list of scores
        sent_score = []
        for sentence in sentences:
            sent_score.append(self.sid.polarity_scores(sentence)['compound'])

        return sent_score

