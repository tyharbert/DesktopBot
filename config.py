scopes = ['identity', 'read', 'submit']


def create(user_agent, app_key, app_secret,
			access_token, refresh_token):
	c = dict()
	c['user_agent'] = user_agent
	c['app_key'] = app_key
	c['app_secret'] = app_secret
	c['access_token'] = access_token
	c['refresh_token'] = refresh_token

	return c
	
def create(cnf, access_token):
	c = dict()
	c['user_agent'] = cnf['user_agent']
	c['app_key'] = cnf['app_key']
	c['app_secret'] = cnf['app_secret']
	c['access_token'] = access_token
	c['refresh_token'] = cnf['refresh_token']

	return c
