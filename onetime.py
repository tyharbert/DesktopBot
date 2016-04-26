# adapted from https://github.com/avinassh/prawoauth2/blob/master/examples/halflife3-bot/onetime.py

import praw
from prawoauth2 import PrawOAuth2Server
import config
import myfile

user_agent = input("Enter user agent: ")
app_key = input("Enter app key: ")
app_secret = input("Enter app secret: ")

reddit_client = praw.Reddit(user_agent=user_agent)

oauthserver = PrawOAuth2Server(reddit_client,
			       app_key=app_key,
			       app_secret=app_secret,
                   state=user_agent,
			       scopes=config.scopes)

# start the server, this will open default web browser
# asking you to authenticate
oauthserver.start()
tokens = oauthserver.get_access_codes()

c = config.create(user_agent, app_key, app_secret, tokens['access_token'], tokens['refresh_token'])

myfile.save('save', c)