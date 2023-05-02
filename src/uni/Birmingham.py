from .University import University
from bs4 import BeautifulSoup

class Birmingham(University):
    def __init__(self):
        pass

    def ScrapeForData(self, isRaw):
        if isRaw:
            print("Scraping for Birmingham data... Printing to console")
        else:
            print("Scraping for Birmingham data... Printing to csv")

    
    def OutputCSV(self):
        pass

    def OutputRaw(self):
        pass