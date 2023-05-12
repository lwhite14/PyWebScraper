from uni.Manchester import Manchester
from uni.Birmingham import Birmingham
from uni.Surrey import Surrey
from uni.Portsmouth import Portsmouth
from uni.RMIT import RMIT

class Scraper(object):
    manchester = Manchester()
    birmingham = Birmingham()
    surrey = Surrey()
    portsmouth = Portsmouth()
    rmit = RMIT()

    def Manchester(self, isRaw, depth, keywords):
        print ("Scraping for data... this might take a while!")
        self.manchester.ScrapeForData(isRaw, depth, keywords)
        print ("---DONE---")

    def Birmingham(self, isRaw, depth, keywords):
        print ("Scraping for data... this might take a while!")
        self.birmingham.ScrapeForData(isRaw, depth, keywords)
        print ("---DONE---")

    def Surrey(self, isRaw, depth, keywords):
        print ("Scraping for data... this might take a while!")
        self.surrey.ScrapeForData(isRaw, depth, keywords)
        print ("---DONE---")

    def Portsmouth(self, isRaw, depth, keywords):
        print ("Scraping for data... this might take a while!")
        self.portsmouth.ScrapeForData(isRaw, depth, keywords)
        print ("---DONE---")

    def RMIT(self, isRaw, depth, keywords):
        print ("Scraping for data... this might take a while!")
        self.rmit.ScrapeForData(isRaw, depth, keywords)
        print ("---DONE---")
