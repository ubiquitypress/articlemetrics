from django.core.management.base import BaseCommand

from core import models
from pprint import pprint

def add_publication_to_queue(publication, source):
		new_queue_object = models.Queue(publication=publication, source=source)
		new_queue_object.save()

		return new_queue_object

class Command(BaseCommand):
	help = 'Adds items to the twitter search Q'

	def add_arguments(self, parser):
		parser.add_argument('sources', nargs='+', type=str)

	def handle(self, *args, **options):
		source_list = options['sources'][0].split(',')
		publication_list = models.Publication.objects.all().order_by('-date_published')


		pprint(source_list)

		for source in source_list:
			for publication in publication_list:
				add_publication_to_queue(publication, source)