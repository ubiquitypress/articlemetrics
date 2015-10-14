import requests
import json
from pprint import pprint

def query(publication):
	url = 'https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch="%s"' % publication.identifier
	r = requests.get(url)
	results = json.loads(r.text)

	return results['query']['search']