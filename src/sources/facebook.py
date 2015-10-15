import facebook
import requests
import json
import pprint

def query_graph_api(token):
	api = facebook.GraphAPI(token)
	api.fql({'query':u"select url, share_count, like_count, comment_count, click_count, total_count from link_stat where url = '%{query_url}'"})

def get_token(client_id, client_secret):
	url = 'https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=client_credentials' % (client_id, client_secret)
	r = requests.get(url)
	return r.text[13:]

def query_links(publication):
	canonical_url = 'https://api.facebook.com/method/links.getStats?urls=%s&format=json' % publication.canonical_url
	doi_url = 'https://api.facebook.com/method/links.getStats?urls=http://dx.doi.org/%s&format=json' % publication.identifier
	ojs_url = 'https://api.facebook.com/method/links.getStats?urls=%s&format=json' % publication.canonical_url_two


	c_request = requests.get(canonical_url)
	d_request = requests.get(doi_url)

	print c_request.text

	if publication.canonical_url_two:
		ojs_request = requests.get(ojs_url)

	c_dict = json.loads(c_request.text)[0]
	d_dict = json.loads(d_request.text)[0]

	if publication.canonical_url_two:
		ojs_dict = json.loads(ojs_request.text)[0]

	facebook_counts = {
		'share_count': 0,
		'like_count': 0,
		'comment_count': 0,
		'click_count': 0,
		'total_count': 0,
	}
	

	if c_request.status_code == 200:
		facebook_counts['share_count'] = c_dict.get('share_count', 0)
		facebook_counts['like_count'] = c_dict.get('like_count', 0)
		facebook_counts['comment_count'] = c_dict.get('comment_count', 0)
		facebook_counts['click_count'] = c_dict.get('click_count', 0)
		facebook_counts['total_count'] = c_dict.get('total_count', 0)

	if d_request.status_code == 200:
		facebook_counts['share_count'] = facebook_counts['share_count'] + d_dict.get('share_count', 0)
		facebook_counts['like_count'] = facebook_counts['like_count'] + d_dict.get('like_count', 0)
		facebook_counts['comment_count'] = facebook_counts['comment_count'] + d_dict.get('comment_count', 0)
		facebook_counts['click_count'] = facebook_counts['click_count']+ d_dict.get('click_count', 0)
		facebook_counts['total_count'] = facebook_counts['total_count'] + d_dict.get('total_count', 0)

	if publication.canonical_url_two and ojs_request.status_code == 200:
		facebook_counts['share_count'] = facebook_counts['share_count'] + ojs_dict.get('share_count', 0)
		facebook_counts['like_count'] = facebook_counts['like_count'] + ojs_dict.get('like_count', 0)
		facebook_counts['comment_count'] = facebook_counts['comment_count'] + ojs_dict.get('comment_count', 0)
		facebook_counts['click_count'] = facebook_counts['click_count']+ ojs_dict.get('click_count', 0)
		facebook_counts['total_count'] = facebook_counts['total_count'] + ojs_dict.get('total_count', 0)

	return facebook_counts