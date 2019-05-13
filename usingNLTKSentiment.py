import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class NLTKSentiment(object):

    def __init__(self):
        # No training here
        self.sid = SentimentIntensityAnalyzer()

    def sentiment(self, text):
        # Get list of sentences
        sentences = nltk.sent_tokenize(text)

        # Create average score for all sentences
        for sentence in sentences:
            print(sentence)
            ss = self.sid.polarity_scores(sentence)
            for k in sorted(ss):
                print('{0}: {1}, '.format(k, ss[k]))
                print()

