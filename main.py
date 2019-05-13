from SentimentFactory import SentimentFactory
from sample_string import sample_string
from collections import defaultdict
import nltk


def main():
    methods = ['TextBlob', 'NLTKSentiment']

    # Store list of scores
    sent_scores = defaultdict(list)

    for method in methods:
        obj = SentimentFactory.factory(method)
        sent_scores[method] = obj.sentiment(sample_string)

    # Get list of sentences
    sentences = nltk.sent_tokenize(sample_string)

    # Get summary table
    print "# {0}".format(sent_scores.keys())
    for idx, sentence in enumerate(sentences):
        score_list = []
        for key in sent_scores.keys():
            score_list.append(sent_scores[key][idx])
        clean_sentence = sentence.replace('\n','')
        print '{0}: {1}, {2}'.format(idx, score_list, clean_sentence)


if __name__ == '__main__':
    main()
