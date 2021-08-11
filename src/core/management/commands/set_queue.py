from itertools import chain, islice
import logging

from django.conf import settings
from django.core.management.base import BaseCommand

from core import models

logger = logging.getLogger('django')


def add_publication_to_queue(publication, source):
        new_queue_object = models.Queue(
            publication=publication,
            source=source
        )

        return new_queue_object


class Command(BaseCommand):
    help = (
        "Adds items to the queue; takes metric type e.g. 'crossref' as "
        "argument"
    )

    def add_arguments(self, parser):
        parser.add_argument('sources', nargs='+', type=str)

    def handle(self, *args, **options):
        logger.info('start set queue')
        source_list = options['sources'][0].split(',')
        publication_list = models.Publication.objects.all().order_by(
            '-date_published'
        )

        queue = chain(
            *(
                (
                    add_publication_to_queue(publication, source)
                    for publication in publication_list
                )
                for source in source_list
            )
        )

        while True:
            batch = list(
                islice(
                    queue,
                    settings.SQL_BULK_INSERT_BATCH_SIZE
                )
            )
            if not batch:
                break
            models.Queue.objects.bulk_create(
                batch,
                settings.SQL_BULK_INSERT_BATCH_SIZE
            )

        logger.info('end set queue')
