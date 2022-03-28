import pandas as pd 

def most_tweets(dataframe):
    new_df = dataframe["user"]
    data = []
    for i in new_df:
        data.append([i["username"], i["statusesCount"]])
    
    aux_2 = pd.DataFrame(data, columns=['username', 'statusesCount'])
    aux_2 = aux_2.nlargest(10, "statusesCount")
    return aux_2