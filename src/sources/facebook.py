import facebook
import requests
import json

def query_graph_api(token):
	api = facebook.GraphAPI(token)
	api.fql({'query':u"select url, share_count, like_count, comment_count, click_count, total_count from link_stat where url = '%{query_url}'"})

def get_token(client_id, client_secret):
	url = 'https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=client_credentials' % (client_id, client_secret)
	r = requests.get(url)
	return r.text[13:]