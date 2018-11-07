import json

from .modules.inkipedia_crawler import InkipediaCrawler
from .modules.inkipedia_parser import InkipediaParser


def save_inkipedia_json():
    base_url = 'https://splatoonwiki.org'
    html_file_name = 'latest_inkipedia.html'
    scrap_name = 'latest_inkipedia.json'

    crawler = InkipediaCrawler(base_url, html_file_name)
    crawler.crawl_main_page()

    parser = InkipediaParser(html_file_name)

    information = dict()
    information['Salmon Run'] = parser.get_salmonrun_schedule()
    information['Regular Battle'] = parser.get_regular_schedule()
    information['Ranked Battle'] = parser.get_ranked_schedule()
    information['League Battle'] = parser.get_league_schedule()

    with open(scrap_name, 'w') as f:
        json.dump(information, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    save_inkipedia_json()
