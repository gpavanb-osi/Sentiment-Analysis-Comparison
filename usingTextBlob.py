import nltk
from textblob import TextBlob


class TextBlobApproach(object):
    def __init__(self):
        pass

    def sentiment(self, text):
        # Get list of sentences
        sentences = nltk.sent_tokenize(text)

        # Create average score for all sentences
        count = 1
        for sentence in sentences:
            print(sentence)
            ss = TextBlob(sentence).sentiment.polarity
            print('{0}: {1}, '.format(count, ss))
            print()
            count += 1
