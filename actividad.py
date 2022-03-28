import pandas as pd
from most_retweeted import most_retweeted 
from most_tweets import most_tweets
from most_days import top_days
from top_hashtags import top_hashtags

def main(file):
    df = pd.read_json(file)
    #print(df)

    p1 = most_retweeted(df)
    print("\nTop 10 tweets mas retweeted")
    print(p1)

    p2 = most_tweets(df)
    print("\nTop 10 usuarios que mas tweets emitieron")
    print(p2)


main('dataset_clean.json')