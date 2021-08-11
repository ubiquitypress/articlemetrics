import json
import logging

import requests

logger = logging.getLogger('django')


def query(publication):
    url = (
        'https://en.wikipedia.org/w/api.php?action=query'
        '&list=search&format=json&srsearch="%s"' % publication.identifier
    )
    logger.info(
        'start wikipedia: {url}'.format(
            url=url
        )
    )
    r = requests.get(url)
    results = json.loads(r.text)

    logger.info(
        'end wikipedia: {url}'.format(
            url=url
        )
    )

    return results['query']['search']
