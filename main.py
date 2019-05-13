import SentimentFactory
from sample_string import sample_string


def main():
    method = 'TextBlob'

    obj = SentimentFactory.factory(method)
    obj.sentiment(sample_string)


if __name__ == '__main__':
    main()
