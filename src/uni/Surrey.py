from .University import University
from bs4 import BeautifulSoup

class Surrey(University):
    def __init__(self):
        pass

    def ScrapeForData(self, isRaw, depth, keywords):
        if isRaw:
            print("Scraping for Surrey data... Printing to console")
        else:
            print("Scraping for Surrey data... Printing to csv")

    
    def OutputCSV(self):
        pass

    def OutputRaw(self):
        pass