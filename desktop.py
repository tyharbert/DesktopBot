import praw
from prawoauth2 import PrawOAuth2Mini
import config
import myfile
import time
import download


cnf = myfile.load('save')

# access reddit
def main():
	while True:
		try:
			print('attempting to connect to reddit api')
			cnf = myfile.load('save')
			reddit_client = praw.Reddit(user_agent=cnf['user_agent'])
			oauth_helper = init(reddit_client)

			print('printing hot 5 posts from r/earthporn')
			download.do_stuff(reddit_client)

			print('sleeping for 4 hours')
			time.sleep(14400)

		except praw.errors.OAuthInvalidToken:
			print('refreshing access_token')
			oauth_helper.refresh()
			tokens = oauth_helper.get_access_codes()
			cnf = config.create(cnf, tokens['access_token'])
			myfile.save('save', cnf)


# intialize oauth authentication
def init(reddit_client):
	oauth_helper = PrawOAuth2Mini(reddit_client,
									app_key=cnf['app_key'],
	                       			app_secret=cnf['app_secret'],
	                        		access_token=cnf['access_token'],
	                        		refresh_token=cnf['refresh_token'],
	                        		scopes=config.scopes)

	return oauth_helper


#call main
if __name__ == '__main__':
    main()