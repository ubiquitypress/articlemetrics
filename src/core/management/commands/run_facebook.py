from django.core.management.base import BaseCommand

from core import models
from sources import facebook
from pprint import pprint

def add_new_citation(publication, citation):

	defaults = {
		'journal_title': citation.get('journal_title'),
		'article_title': citation.get('article_title'),
		'volume': citation.get('volume'),
		'issue': citation.get('issue'),
		'year': citation.get('year'),
	}

	new_citation, created = models.Citation.objects.get_or_create(publication=publication, doi=citation.get('doi'), defaults=defaults)

	if created:
		print 'Citation created for %s, %s - %s' % (publication.title, citation.get('doi'), citation.get('article_title'))
	else:
		print 'Citation already exists.'

class Command(BaseCommand):
	help = 'Queries crossref.'

	def handle(self, *args, **options):
		q = models.Queue.objects.filter(source='facebook')

		for item in q:
			facebook_count = facebook.query_links(item.publication)

			new_facebook, created = models.Facebook.objects.update_or_create(publication=item.publication, defaults=facebook_count)

			if created:
				print 'Facebook metrics created.'
			else:
				print 'Facebook metrics updated'
