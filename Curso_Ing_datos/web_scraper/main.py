#web scraper sitios de noticias
import argparse
#libreria que permite enviar mensajes por consola de manera automatica asignando nivel de importacia
import logging
logging.basicConfig(level=logging.INFO)
from common import config

logger=logging.getLogger(__name__)
def _news_scraper(new_sites):

    host = config()['news_sites'][new_sites]
    return logging.info('Beginning scraper for {}'.format(host))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    news_site_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_site',
                         help='the news site that you want to scrape',
                         type=str,
                         choices=news_site_choices)
        
    args = parser.parse_args()
    _news_scraper(args.news_site)

