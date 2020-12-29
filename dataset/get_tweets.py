import pandas as pd
import tweepy as tw

consumer_key = 'yourkeyhere'
consumer_secret = 'yourkeyhere'
access_token = 'yourkeyhere'
access_token_secret = 'yourkeyhere'
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)

# Collect tweets
date_since = "2018-11-16"
loca = [-105.292778 40.019444 25mi]
tweets = tw.Cursor(api.search,
              q=search_words,
              geocode="37.781157,-122.398720,100mi",
              since=date_since).items(5)

# Iterate and print tweets
for tweet in tweets:
    print(tweet.text)

tweet_df = pd.DataFrame(data=users_locs,
                    columns=['user', "location"])
