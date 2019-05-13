import usingTextBlob
import usingNLTKSentiment


class SentimentFactory(object):

    @staticmethod
    def factory(method=''):
        if method == 'TextBlob':
            print "Using TextBlob for sentiment analysis..."
            return usingTextBlob.TextBlobApproach()
        elif method == 'NLTKSentiment':
            print "Using NLTKSentiment for sentiment analysis..."
            return usingNLTKSentiment.NLTKSentiment()
