import tweepy
import random
import numpy as np

consumer_key = "ENTERCONSUMERKEY"
consumer_secret = "ENTERCONSUMERSECRETKEY"
access_token = "ENTERACCESSTOKEN"
access_token_secret = "ENTERACCESSTOKENSECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

#Put the Give-away tweet ID here
GA_ID = 1321156151515

GA_TWEET = api.get_status(GA_ID)
NEW_SEARCH_TERM = 'RT @' + GA_TWEET.user.screen_name + ': ' + GA_TWEET.text[0:50]
print("The give-away tweet:")
print(NEW_SEARCH_TERM + '\n')
GA_RT2LIST = []

for tweet in tweepy.Cursor(api.search,
                           q=NEW_SEARCH_TERM,
                           count=1000,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
    GA_RT2LIST.append(tweet)

GA_RT_Names = []
print("Number of public retweets collected:")
print(len(GA_RT2LIST))

for item in GA_RT2LIST:
    GA_RT_Names.append(item.user.screen_name)
print(GA_RT_Names)

# If you want to use a different randomizer, you can get the csv
# of the names of the twitter user names of the participants.
np.savetxt("CSVNAME.csv", GA_RT_Names, delimiter=",", fmt='%s')

# If running on google colab, the csv file will be on the files tab (folder icon)

print("\nWINNER:")
print(random.choice(GA_RT_Names))