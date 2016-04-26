# Desktop Bot

This will use python to retrive hot posts from reddit and make them the desktop background.

# Requirments

[praw](https://praw.readthedocs.org/en/stable/)
[prawoauth2](https://pypi.python.org/pypi/prawoauth2/0.2.1)
[simplejson](https://pypi.python.org/pypi/simplejson/)

# Operation Instructions

1. Create your app on reddit by clicking [here](https://www.reddit.com/prefs/apps/) and selecting "are you a developer? create an app..." at the bottom of the page

2. After creating your app you must note your app_key (value under the app name) and the app_secret (this is the long string of characters under the app_key) NOTE: do not share this with anyone!

3. Run onetime.py which I adapted from [this repo](https://github.com/avinassh/prawoauth2/blob/master/examples/halflife3-bot/onetime.py).  This will launch a default browser instance where you must confirm you want to authenticate the app. This uses myfile.py to automatically save the information you have entered, as well as the access_token and refresh_token retrived, to the file 'save'. DO NOT SHARE your app secret with anyone, that is in this file!

4. Run desktop.py. This is setup to read your credentials from the file 'save' and automatically update your access_token when it expires. An access token lasts 60 minutes so the previous will be read in from the file until it has expired
