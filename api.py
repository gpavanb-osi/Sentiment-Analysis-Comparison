import nltk
import pandas as pd
from SentimentFactory import SentimentFactory
from collections import defaultdict


def get_scores(methods, text):
    # Scores
    scores = {}
    print("Methods:", methods)
    # Get list of sentences
    sentences = nltk.sent_tokenize(text)

    for method in methods:
        obj = SentimentFactory.factory(method)
        score_list = []
        for sentence in sentences:
            clean_sentence = sentence.replace('\n','')
            score_list.append(obj.sentiment(clean_sentence)[0])

        # Round the results
        score_list = [round(x, 2) for x in score_list]
        scores[method] = score_list

    scores["Sentences"] = sentences
    # Convert scores to dataframe
    return pd.DataFrame(scores)


    
