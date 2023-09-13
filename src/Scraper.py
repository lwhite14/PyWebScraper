from uni.Manchester import Manchester
from uni.Birmingham import Birmingham
from uni.Surrey import Surrey
from uni.Portsmouth import Portsmouth
from uni.RMIT import RMIT
from uni.Sheffield import Sheffield
from uni.Leeds import Leeds
from uni.York import York
from uni.UWE import UWE
from uni.Lancaster import Lancaster
from uni.Aberdeen import Aberdeen
from uni.BathSpa import BathSpa
from uni.Exeter import Exeter

class Scraper(object):
    manchester = Manchester()
    birmingham = Birmingham()
    surrey = Surrey()
    portsmouth = Portsmouth()
    rmit = RMIT()
    sheffield = Sheffield()
    leeds = Leeds()
    york = York()
    uwe = UWE()
    lancaster = Lancaster()
    aberdeen = Aberdeen()
    bathSpa = BathSpa()
    exeter = Exeter()

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

    def Sheffield(self, isRaw, depth, keywords):
        print ("Scraping for data... this might take a while!")
        self.sheffield.ScrapeForData(isRaw, depth, keywords)
        print ("---DONE---")

    def Leeds(self, isRaw, depth, keywords):
        print ("Scraping for data... this might take a while!")
        self.leeds.ScrapeForData(isRaw, depth, keywords)
        print ("---DONE---")

    def York(self, isRaw, depth, keywords):
        print ("Scraping for data... this might take a while!")
        self.york.ScrapeForData(isRaw, depth, keywords)
        print ("---DONE---")

    def UWE(self, isRaw, depth, keywords):
        print ("Scraping for data... this might take a while!")
        self.uwe.ScrapeForData(isRaw, depth, keywords)
        print ("---DONE---")

    def Lancaster(self, isRaw, depth, keywords):
        print ("Scraping for data... this might take a while!")
        self.lancaster.ScrapeForData(isRaw, depth, keywords)
        print ("---DONE---")

    def Aberdeen(self, isRaw, depth, keywords):
        print ("Scraping for data... this might take a while!")
        self.aberdeen.ScrapeForData(isRaw, depth, keywords)
        print ("---DONE---")

    def BathSpa(self, isRaw, depth, keywords):
        print ("Scraping for data... this might take a while!")
        self.bathSpa.ScrapeForData(isRaw, depth, keywords)
        print ("---DONE---")

    def Exeter(self, isRaw, depth, keywords):
        print ("Scraping for data... this might take a while!")
        self.exeter.ScrapeForData(isRaw, depth, keywords)
        print ("---DONE---")
