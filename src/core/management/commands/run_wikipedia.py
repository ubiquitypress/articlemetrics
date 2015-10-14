from django.core.management.base import BaseCommand

from core import models
from sources import wikipedia
from pprint import pprint
import time

def add_new_citation(publication, citation):

	defaults = {
		'snippet': citation.get('snippet'),
		'timestamp': citation.get('timestamp'),
	}

	new_citation, created = models.Wikipedia.objects.get_or_create(publication=publication, title=citation.get('title'), defaults=defaults)

	if created:
		print 'Citation created for %s, %s - %s' % (publication.identifier, citation.get('title'))
	else:
		print 'Citation already exists.'

class Command(BaseCommand):
	help = 'Queries wikipedia.'

	def handle(self, *args, **options):
		q = models.Queue.objects.filter(source='wikipedia')

		for item in q:
			wiki_list = wikipedia.query(item.publication)
			print 'Requesting %s' % item.publication.identifier

			if wiki_list:
				for citation in wiki_list:
					pprint(citation)
					add_new_citation(item.publication, citation)

			print "Waiting for 4 seconds before requesting again"
			time.sleep(4)
