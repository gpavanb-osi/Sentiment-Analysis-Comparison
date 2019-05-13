import nltk
from textblob import TextBlob


class TextBlobApproach(object):
    def __init__(self):
        pass

    def sentiment(self, text):
        # Get list of sentences
        sentences = nltk.sent_tokenize(text)

        # Return list of scores
        sent_score = []
        for sentence in sentences:
            sent_score.append(TextBlob(sentence).sentiment.polarity)

        return sent_score
