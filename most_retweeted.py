def most_retweeted(dataframe):
    new_df = dataframe[["content", "retweetCount"]]
    new_df = new_df.nlargest(10, "retweetCount")
    return new_df