import nltk
import re
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('punkt')

'''
Sentiment is parsed from tweets
INPUT: interval_lists- list of lists that store cleaned tweet text for each interval
OUTPUT: all_sentiment- list of lists of identical dimensions to the input list that stores sentiment scores for each tweet
RESULTS: The sentiment parsed from the tweets can be used to gauge change in sentiment over time
'''
def parse(interval_lists):
    
    #initialize sentiment analysis tool
    sia = SentimentIntensityAnalyzer()
    #create lists to store sentiment analysis scores in a format that mimics the interval_lists fed as input to this method
    sent_list = [] #temp sublist of all_sentiment
    all_sentiment = [] #this list is returned
    
    #list of words that are meaningless to sentiment analysis
    stopwords = nltk.corpus.stopwords.words("english")
    
    #use all meaningful words in the strings within interval_lists to parse sentiment and store the sentiment within all_sentiment
    for interval in interval_lists:
        for tweet in interval:
            word_tokens = word_tokenize(tweet)
            words = [w + " " for w in word_tokens if w not in stopwords]
            words = "".join(words)
            #use the compound score to represent sentiment score
            sent_list.append(sia.polarity_scores(words)['compound'])
        all_sentiment.append(sent_list.copy())
        sent_list.clear()
        
    return all_sentiment
'''
sia vader 
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
'''