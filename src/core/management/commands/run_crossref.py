from itertools import chain, islice
import logging

from django.conf import settings
from django.core.management.base import BaseCommand

from core import models
from sources import crossref

logger = logging.getLogger('django')


def add_new_citation(citation):
    kwargs = {
        'publication': citation.get('publication'),
        'doi': citation.get('doi'),
        'journal_title': citation.get('journal_title'),
        'article_title': citation.get('article_title'),
        'volume': citation.get('volume'),
        'issue': citation.get('issue'),
        'year': citation.get('year'),
    }

    new_citation = models.Citation(
        **kwargs
    )

    return new_citation


def citations_generator(queue):
    for citations in (
            crossref.get_crossref_citations(
                item.publication.publisher.crossref_username,
                item.publication.publisher.crossref_password,
                item.publication
            )
            for item in queue
    ):
        yield citations


class Command(BaseCommand):
    help = 'Queries crossref.'

    def handle(self, *args, **options):
        logger.info('start run_crossref')
        queue = models.Queue.objects.filter(
            source='crossref'
        )

        try:
            batch_generator = (
                add_new_citation(citation)
                for citation in chain(
                        *(
                            citations_generator(queue)
                        )
                )
                if not models.Citation.objects.filter(
                        publication=citation.get('publication'),
                        doi=citation.get('doi')
                )
            )
            while True:
                batch = list(
                    islice(
                        batch_generator,
                        settings.SQL_BULK_INSERT_BATCH_SIZE
                    )
                )
                if not batch:
                    break
                models.Citation.objects.bulk_create(
                    batch,
                    settings.SQL_BULK_INSERT_BATCH_SIZE
                )
        finally:
            queue.delete()

        logger.debug('end run_crossref')
