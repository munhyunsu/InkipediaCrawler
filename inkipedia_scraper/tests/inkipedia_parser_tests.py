import unittest
import datetime

from bs4 import BeautifulSoup

from inkipedia_scraper.inkipedia_parser import InkipediaParser

TEST_HTML = 'inkipedia_scraper/tests/inkipedia_parser_tests.html'
SALMONRUN_GT = [{'start_time': datetime.datetime(2021, 4, 16, 21,
                                                 tzinfo=datetime.timezone(datetime.timedelta(hours=9))).isoformat(),
                 'end_time': datetime.datetime(2021, 4, 18, 15,
                                               tzinfo=datetime.timezone(datetime.timedelta(hours=9))).isoformat(),
                 'weapon1': 'Sloshing Machine',
                 'weapon2': 'Splattershot',
                 'weapon3': 'Splat Charger',
                 'weapon4': 'Random',
                 'stage': 'Lost Outpost',
                 'reward': 'Beekeeper Hat'},
                {'start_time': datetime.datetime(2021, 4, 18, 21,
                                                 tzinfo=datetime.timezone(datetime.timedelta(hours=9))).isoformat(),
                 'end_time': datetime.datetime(2021, 4, 20, 9,
                                               tzinfo=datetime.timezone(datetime.timedelta(hours=9))).isoformat(),
                 'weapon1': 'Glooga Dualies',
                 'weapon2': 'Splattershot Pro',
                 'weapon3': 'Slosher',
                 'weapon4': 'Classic Squiffer',
                 'stage': 'Marooner\'s Bay',
                 'reward': 'Office Attire'}]
REGULAR_GT = [{'rule': 'Turf War',
               'stage1': 'Starfish Mainstage',
               'stage2': 'The Reef'},
              {'rule': 'Turf War',
               'stage1': 'Manta Maria',
               'stage2': 'Sturgeon Shipyard'}]
RANKED_GT = [{'rule': 'Splat Zones',
              'stage1': 'Snapper Canal',
              'stage2': 'Ancho-V Games'},
             {'rule': 'Clam Blitz',
              'stage1': 'Moray Towers',
              'stage2': 'Musselforge Fitness'}]
LEAGUE_GT = [{'rule': 'Rainmaker',
              'stage1': 'Blackbelly Skatepark',
              'stage2': 'Piranha Pit'},
             {'rule': 'Tower Control',
              'stage1': 'Inkblot Art Academy',
              'stage2': 'Goby Arena'}]


class InkipediaParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = InkipediaParser(TEST_HTML)

    def tearDown(self):
        del self.parser

    def test___init__(self):
        self.assertIsInstance(self.parser.soup, BeautifulSoup)

    def test_get_salmonrun_schedule(self):
        self.assertEqual(SALMONRUN_GT, self.parser.get_salmonrun_schedule())

    def test_get_regular_schedule(self):
        self.assertEqual(REGULAR_GT, self.parser.get_regular_schedule())

    def test_get_ranked_schedule(self):
        self.assertEqual(RANKED_GT, self.parser.get_ranked_schedule())

    def test_get_league_schedule(self):
        self.assertEqual(LEAGUE_GT, self.parser.get_league_schedule())
