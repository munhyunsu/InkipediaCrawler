import unittest
import os
import datetime

from bs4 import BeautifulSoup

from modules.inkipedia_parser import InkipediaParser

TEST_HTML = 'inkipedia_parser_tests.html'
SALMONRUN_GT = [{'start_time': datetime.datetime(2018, 8, 20, 3,
                                                 tzinfo=datetime.timezone(datetime.timedelta(hours=9))).isoformat(),
                 'end_time': datetime.datetime(2018, 8, 21, 9,
                                               tzinfo=datetime.timezone(datetime.timedelta(hours=9))).isoformat(),
                 'weapon1': 'Squeezer',
                 'weapon2': 'Mini Splatling',
                 'weapon3': 'Undercover Brella',
                 'weapon4': 'Classic Squiffer',
                 'stage': 'Marooner\'s Bay'},
                {'start_time': datetime.datetime(2018, 8, 21, 21,
                                                 tzinfo=datetime.timezone(datetime.timedelta(hours=9))).isoformat(),
                 'end_time': datetime.datetime(2018, 8, 23, 3,
                                               tzinfo=datetime.timezone(datetime.timedelta(hours=9))).isoformat(),
                 'weapon1': 'Splattershot',
                 'weapon2': 'Slosher',
                 'weapon3': 'Octobrush',
                 'weapon4': 'E-liter 4K Scope',
                 'stage': 'Salmonid Smokeyard'}]
REGULAR_GT = [{'time': 'Now',
               'rule': 'Turf War',
               'stage1': 'Ancho-V Games',
               'stage2': 'Musselforge Fitness'},
              {'time': 'Next',
               'rule': 'Turf War',
               'stage1': 'Arowana Mall',
               'stage2': 'Walleye Warehouse'}]
RANKED_GT = [{'time': 'Now',
              'rule': 'Clam Blitz',
              'stage1': 'Inkblot Art Academy',
              'stage2': 'Sturgeon Shipyard'},
             {'time': 'Next',
              'rule': 'Splat Zones',
              'stage1': 'Ancho-V Games',
              'stage2': 'Piranha Pit'}]
LEAGUE_GT = [{'time': 'Now',
              'rule': 'Rainmaker',
              'stage1': 'Camp Triggerfish',
              'stage2': 'Wahoo World'},
             {'time': 'Next',
              'rule': 'Tower Control',
              'stage1': 'New Albacore Hotel',
              'stage2': 'Humpback Pump Track'}]


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
