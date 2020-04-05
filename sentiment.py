import csv

#perform sentiment analysis on tweets    
with open('sentiment.csv', 'r') as f:
    rows = csv.reader(f)
    for r in rows:
        print(r)
    #sentiment_of_tweet = [["Positive"] if TextBlob(r[0]).sentiment.polarity >= 0 else ["Negative"] for r in rows]

