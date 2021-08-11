import logging

from django.core.management.base import BaseCommand

from core import models
from sources import facebook
import time

logger = logging.getLogger('django')


def add_new_citation(publication, citation):

    defaults = {
        'journal_title': citation.get('journal_title'),
        'article_title': citation.get('article_title'),
        'volume': citation.get('volume'),
        'issue': citation.get('issue'),
        'year': citation.get('year'),
    }

    new_citation, created = models.Citation.objects.get_or_create(
        publication=publication,
        doi=citation.get('doi'),
        defaults=defaults
    )

    if created:
        print(
            'Citation created for %s, %s - %s' % (
                publication.title,
                citation.get('doi'),
                citation.get('article_title')
            )
        )
    else:
        print('Citation already exists.')


class Command(BaseCommand):
    help = 'Queries facebook.'

    def handle(self, *args, **options):
        logger.info('start facebook queue')
        queue = models.Queue.objects.filter(source='facebook')

        for item in queue:
            facebook_count = facebook.query_links(item.publication)

            new_facebook, created = models.Facebook.objects.update_or_create(
                publication=item.publication,
                defaults=facebook_count
            )

            item.delete()
            time.sleep(4)

        logger.info('end facebook queue')
