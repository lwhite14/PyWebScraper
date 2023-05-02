from uni.Manchester import Manchester
from uni.Birmingham import Birmingham
from uni.Surrey import Surrey

class Scraper(object):
    manchester = Manchester()
    birmingham = Birmingham()
    surrey = Surrey()

    def Manchester(self, isRaw):
        self.manchester.ScrapeForData(isRaw)

    def Birmingham(self, isRaw):
        self.birmingham.ScrapeForData(isRaw)

    def Surrey(self, isRaw):
        self.surrey.ScrapeForData(isRaw)
