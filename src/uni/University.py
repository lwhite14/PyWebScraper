from abc import ABC, abstractmethod
import csv

class University(ABC):
    titleArr = []
    hrefArr = []
    authorArr = []
    dateArr = []
    abstractArr = []
    keywordsArr = []

    @abstractmethod
    def ScrapeForData(self, isRaw, depth, keywords):
        pass

    def OutputCSV(self, uniNameFull, csvName):
        with open('out/' + csvName + '.csv', 'w', newline='', encoding='utf-8') as csvFile:
            headerList = ['Title', 'Href', 'Author', 'Date', 'Abstract', 'Keywords', 'University Name']
            writer = csv.DictWriter(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, fieldnames=headerList)
            writer.writeheader()
            for x in range(len(self.titleArr)):
                abstract = self.abstractArr[x].replace('\n', ' ').replace('\r', '')
                writer.writerow({'Title': self.titleArr[x], 'Href': self.hrefArr[x], 'Author': self.authorArr[x], 'Date': self.dateArr[x], 'Abstract': abstract, 'Keywords': self.keywordsArr[x], 'University Name': uniNameFull})


    def OutputRaw(self, uniNameFull):
        print("Title,Href,Author,Date,Abstract,Keyword,University Name")
        for x in range(len(self.arr)):
            print(self.titleArr[x] + ',' + self.hrefArr[x] + ',' + self.authorArr[x] + ',' + self.dateArr[x] + ',' + self.abstractArr[x] + ',' + self.keywordsArr[x] + ', ' + uniNameFull)