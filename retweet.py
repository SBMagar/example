# import os
# import sys
# import time
# import random
# import tweepy
# from dotenv import load_dotenv
# from termcolor import colored

# #To make the .env file accessible as the source of environment variables
# load_dotenv()

# #Accessing credentials from .env file
# CONSUMER_KEY = os.getenv("CONSUMER_KEY")
# CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
# ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
# ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
# BEARER_TOKEN = os.getenv("BEARER_TOKEN")
# CLIENT_ID = os.getenv("CLIENT_ID")
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# CALLBACK_URI = os.getenv("CALLBACK_URI")

# #Setting credentials to access Twitter API
# # auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# # auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# # api = tweepy.Client(
# #     bearer_token=BEARER_TOKEN,
# #     consumer_key=CONSUMER_KEY,
# #     consumer_secret=CONSUMER_SECRET,
# #     access_token=ACCESS_TOKEN,
# #     access_token_secret=ACCESS_TOKEN_SECRET,
# #     wait_on_rate_limit=True
# # )

# oauth2_user_handler = tweepy.OAuth2UserHandler(client_id=CLIENT_ID,
#                         client_secret=CLIENT_SECRET,
#                         redirect_uri=CALLBACK_URI,
#                         scope=['tweet.read', 'tweet.write', 'users.read'])

# print(oauth2_user_handler.get_authorization_url())

# authorization_response = input('Paste redirect url here:  ')

# # fetch access token
# access_token = oauth2_user_handler.fetch_token(authorization_response)

# # initialize client with consumer and access tokens
# api = tweepy.Client(access_token["access_token"])

# # #Calling API using Tweepy
# # api = tweepy.API(auth, wait_on_rate_limit=True)

# #Search Twitter for tweets with this keyword
# #Put multiple keywords with 'OR' in between
# #Example: search = '#keywordToSearch OR #keywordToSearch2'
# search = '#taylorswift OR #devops OR #python OR #AI OR #cloud OR #AWS'

# #Maximum limit of tweets to be interacted with
# maxNumberOfTweets = 500

# #To keep track of tweets published
# count = 0

# print(colored('Retweet Bot Started!', 'green'))

# for tweet in tweepy.Paginator(api.search_recent_tweets, search).flatten(maxNumberOfTweets):
#     try:
#         print(colored('Found tweet by @' + tweet.user.screen_name, 'cyan'))

#         #Publishing retweet
#         tweet.retweet()

#         #Updating count for each successfull retweet
#         count = count + 1
#         print(colored('Retweet #' + str(count) + ' published successfully.', 'green'))

#         #Random wait time
#         timeToWait = random.randint(95, 115)
#         print("Waiting for "+ str(timeToWait) + " seconds")
#         for remaining in range(timeToWait, -1, -1):
#             sys.stdout.write("\r")
#             sys.stdout.write("{:2d} seconds remaining.".format(remaining))
#             sys.stdout.flush()
#             time.sleep(1)
#         sys.stdout.write("\rOnwards to next tweet!\n")

#     except tweepy.TweepError as e:
#         print('Error: ' + e.args[0][0]['message'])
#     except StopIteration:
#         break

# # https://twitter.com/S_agarM_agar&scope=tweet.read+tweet.write+users.read&state=FoNosZGSbM8x7sRfaqw2Au0baXjDEa&code_challenge=JZhEEILLYDScgQuvPfF6gDcaIEWhRqMpO7mUloTWccA&code_challenge_method=S256


import os
import sys
import time
import random
import tweepy
from dotenv import load_dotenv
from termcolor import colored

#To make the .env file accessible as the source of environment variables
load_dotenv()

#Accessing credentials from .env file
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

#Setting credentials to access Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#Calling API using Tweepy
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Search Twitter for tweets with this keyword
#Put multiple keywords with 'OR' in between
#Example: search = '#keywordToSearch OR #keywordToSearch2'
search = '#AI OR #Linux OR #IoT OR #blockchain OR #MLOps OR #devops OR #python OR #aws OR #cloudcomputing OR #cicd OR #kubernetes OR #helm'

#Maximum limit of tweets to be interacted with
maxNumberOfTweets = 500

#To keep track of tweets published
count = 0

print(colored('Retweet Bot Started!', 'green'))

for tweet in tweepy.Cursor(api.search, search).items(maxNumberOfTweets):
    try:
        print(colored('Found tweet by @' + tweet.user.screen_name, 'cyan'))

        #Publishing retweet
        tweet.retweet()

        #Updating count for each successfull retweet
        count = count + 1
        print(colored('Retweet #' + str(count) + ' published successfully.', 'green'))

        #Random wait time
        timeToWait = random.randint(5, 20)
        print("Waiting for "+ str(timeToWait) + " seconds")
        for remaining in range(timeToWait, -1, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\rOnwards to next tweet!\n")

    except tweepy.TweepError as e:
        print('Error: ' + e.args[0][0]['message'])
    except StopIteration:
        break
