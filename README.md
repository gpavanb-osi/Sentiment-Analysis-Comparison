# Sentiment-Analysis-Comparison

## Description

This repository provides a generic framework for implementing multiple sentiment analysis
comparison methods and provides a summary for the same. Additional methods can also
be easily implemented by extending the current framework.

## How to Use?

Simply by running `main.py`, one can run all the implemented sentiment analysis methods.

A sample output is as follows

\# ['TextBlob', 'NLTKSentiment']  
0: [0.22727272727272727, 0.5574], This is a positive statement.  
1: [0.22727272727272727, 0.802], Be positive, see positive.  
2: [0.36363636363636365, 0.7579], This will surely read as a positive statement.  
3: [-0.65, -0.8442], But then something evil happens and negative statements need to be identified.  
4: [-0.2333333333333333, -0.7184], Check if minus and negative things give a negative value.  
5: [0.34015151515151515, 0.8555], We are back to good,easy, positive statements.  

## How to Extend?

One can add new sentiment analysis methods by creating a new class, preferably in the format 
`using%`, with `%` standing for a generic class. This must implement a `sentiment` method
which takes in a multi-line string and returns a list of sentiment scores between -1 and +1.

## Whom to Contact?

All questions can be directed to [OSI Digital](https://www.osidigital.com) 

