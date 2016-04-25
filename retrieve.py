import praw

# intialize praw
r = praw.Reddit(user_agent='desktop_changer_test by u/ty_durden',
		site_name='desktop_dev')

# get top 5 hot r/earthporn submissions
submissions = r.get_subreddit('earthporn').get_hot(limit=5)
[str(x) for x in submissions]
