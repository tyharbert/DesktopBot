# used once to allow oauth

import praw
from prawoauth2 import PrawOAuth2Server

user_agent = 'desktop_changer_test by /u/ty_durden'
site_name = 'desktop_dev'
scopes = ['identity', 'read', 'submit']
app_key = ''
app_secret = ''

reddit_client = praw.Reddit(user_agent=user_agent,
				site_name='desktop_dev')

oauthserver = PrawOAuth2Server(reddit_client,
			       app_key=app_key,
			       app_secret=app_secret,
                               state=user_agent,
			       scopes=scopes)

# start the server, this will open default web browser
# asking you to authenticate
oauthserver.start()
tokens = oauthserver.get_access_codes()
print(tokens)
