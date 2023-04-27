import sys
import argparse
from scraper import Scraper

class CustomParser(argparse.ArgumentParser):
	def error(self, message):
		self.print_help()
		sys.exit(2)

class PyUniScraper(object):
	scraper = Scraper();

	def __init__(self):
		parser = CustomParser(
			usage='''PyUniScraper <university> [<options>]
			
The three Universities avaiable to parse for academic material are:
  manchester	Parse for the University of Manchester
  birmingham	Parse for the University of Birmingham
  surrey		Parse for the University of Surrey

Input options:
  -r --raw		Output the data to the console (rather than to a .csv)''')
	
		parser.add_argument('university', help='University to get information for')
		parser.add_argument('-v', '--version', action='version', version='PyUniScraper v0.0.1')
		args = parser.parse_args(sys.argv[1:2])
		if args.university == "manchester":
			self.scraper.Manchester();
		if args.university == "birmingham":
			self.scraper.Birmingham();
		if args.university == "surrey":
			self.scraper.Surrey();
		

if __name__ == '__main__':
	PyUniScraper()