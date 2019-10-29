from datetime import date

from bs4 import BeautifulSoup
import requests


def get_crossref_citations(username, password, publication):
    url = (
        'http://doi.crossref.org/servlet/getForwardLinks?'
        'usr=%s&pwd=%s&doi=%s&startDate=1900-01-01&endDate=%s-12-31' % (
            username, password, publication.identifier, date.today().year
        )
    )
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "xml")

    cr_list = []
    for item in soup.find_all('journal_cite'):
        cr_list.append(
            {
                'publication': publication,
                'doi': item.find('doi').text,
                'journal_title': item.find('journal_title').text,
                'article_title': item.find('article_title').text if item.find(
                    'article_title'
                ) else '[Title not found]',
                'volume': item.find('volume').text if item.find(
                    'volume'
                ) else None,
                'issue': item.find('issue').text if item.find(
                    'issue'
                ) else None,
                'year': item.find('year').text if item.find('year') else None,
            }
        )

    return cr_list
