import pandas as pd
import tweepy as tw
import numpy as np


def show_info(tweet):
    print('User info :',tweet.user.screen_name, tweet.user.id_str)
    print('Text :',tweet.text) #+ "| " + tweet.place.name if tweet.place else "Undefined place")
    print('Place :',tweet.place.name)
    print('Reply info :',tweet.in_reply_to_screen_name, tweet.in_reply_to_user_id_str)
    print('Conversation id :', tweet.conversation_id)
    print('Is quoted :',tweet.is_quote_status)#, tweet.quoted_status_id_str)
    if tweet.text.startswith("RT @") == True: print('Is retweet : True')
    else: print('Is retweet : False')
    print('Retweet count :',tweet.retweet_count)
    print('Time :', tweet.created_at)


consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

# Collect tweets
search_terms = ""
date_since = "2020-12-23"
#places = api.geo_search(query='Belgium', granularity="country")
#place_id = places[0].id
tweets = tw.Cursor(api.search, q='{}'.format(search_terms),since=date_since, geocode="50.8466,04.3528,10km").items(100000)

# Iterate and print tweets
info = []
for tweet in tweets:
    #print(tweet.text)
    if hasattr(tweet.place, "name"): pl = tweet.place.name
    else: pl=None
    info.append([tweet.user.screen_name,
                 tweet.user.id_str,
                 pl,
                 tweet.in_reply_to_screen_name,
                 tweet.in_reply_to_user_id_str,
                 #tweet.conversation_id,
                 tweet.is_quote_status,
                 tweet.text.startswith("RT @"),
                 tweet.created_at])
print(len(info))
tweet_df = pd.DataFrame(data=info, columns=['user', 'user_id', 'location', 'is_reply_to', 'reply_id', 'is_quoted', 'is_rt', 'time'])
print(tweet_df)
tweet_df.to_csv('tweeter_data.csv')
