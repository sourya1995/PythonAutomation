import argparse
import requests
import logging
import http.client
import re
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

DEFAULT_PHRASE = 'python'

def process_link(source_link, text):
    logging.info(f'Extracting links from {source_link}')
    parsed_source = urlparse(source_link)
    result = requests.get(source_link)
    if result.status_code != http.client.OK:
        logging.error(f'Error retrieving {source_link}: {result}')
        return []
    
    if 'html' not in result.headers['Content-Type']:
        logging.info(f'Link {source_link} is not an HTML page')
        return []
    
    page = BeautifulSoup(result.text, 'html.parser')
    search_text(source_link, page, text)

    return get_links(parsed_source, page) 


def get_links(parsed_source, page):
    links = []
    for element in page.find_all('a'):
        link = element.get('href')
        if not link:
            continue

        if link.startswith('#'):
            continue

        if link.startswith('mailto:'):
            continue

        if not link.startswith('http'):
            netloc = parsed_source.netloc
            scheme = parsed_source.scheme
            path = urljoin(parsed_source.path, link)
            link = f'{scheme}://{netloc}{path}'

        if parsed_source.netloc not in link:
            continue

        links,append(link)

    return links

def search_text(source_link, page, text):
    for element in page.find_all(text=re.compile(text, flags=re.IGNORECASE)):
        print(f'Link {source_link}: --> {element}')


def main(base_url, to_search):
    checked_links = set()
    to_check = [base_url]
    max_checks = 10

    while to_check and max_checks:
        link = to_check.pop(0)
        links = process_link(link, text=to_search)
        checked_links.add(link)
        for link in links:
            if link not in checked_links:
                checked_links.add(link)
                to_check.append(link)
        max_checks -= 1



if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(dest='url', type=str, help='Base site url')
    parser.add_argument('-p', type=str, help=f'Sentence to search, default: {DEFAULT_PHRASE}', default=DEFAULT_PHRASE)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    main(args.url, args.p)



        