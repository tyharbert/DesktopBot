import praw


# get top 5 hot r/earthporn submissions
def do_stuff(reddit_client):
	submissions = reddit_client.get_subreddit('earthporn').get_hot(limit=5)
	for submission in submissions:
		print(str(submission))