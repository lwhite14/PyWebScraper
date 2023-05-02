import sys
import argparse
from Scraper import Scraper

class CustomParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_help()
        sys.exit(2)


class PyUniScraper(object):
    def __init__(self):
        scraper = Scraper()
        parser = CustomParser()

        parser.add_argument('university', help='University to get information for')
        parser.add_argument('--raw', dest='raw', action='store_const', const=True, default=False, help='Output to console instead of csv')
        parser.add_argument('-v', '--version', action='version', version='PyUniScraper v0.0.1')
        args = parser.parse_args()
        if args.university == "manchester":
            scraper.Manchester(args.raw)
        if args.university == "birmingham":
            scraper.Birmingham(args.raw)
        if args.university == "surrey":
            scraper.Surrey(args.raw)