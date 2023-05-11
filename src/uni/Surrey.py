from .University import University
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import csv

class Surrey(University):
    titleArr = []
    hrefArr = []
    authorArr = []
    dateArr = []
    abstractArr = []
    keywordsArr = []

    def __init__(self):
        pass


    def ScrapeForData(self, isRaw, depth, keywords):
        for i in range(len(keywords)):
            for y in range(depth):
                url = 'https://openresearch.surrey.ac.uk/esploro/search/outputs?query=any,contains,' + keywords[i] + '&page=' + str(y+1) + '&scope=Research&institution=44SUR_INST'
                page = requests.get(url)

                if page.status_code == 200:
                    soup = BeautifulSoup(page.text, 'html.parser')
                    spans = soup.find_all('span', {'class': 'brief-body'})

                    print(soup.prettify())
                    print(str(len(spans)))

                    for x in tqdm(range(len(spans)), ncols=80, ascii=True, desc=keywords[i] + '; Page ' + str(1 + y)):
                        if not x == 0:
                            self.titleArr.append(spans[x].find('a').get_text())
                            self.hrefArr.append(spans[x].find('a').get('href'))
                            self.authorArr.append(self.GetAuthors(spans[x]))
                            self.dateArr.append(self.GetDate(spans[x]))
                            self.abstractArr.append(self.GetAbstract(spans[x]))
                            self.keywordsArr.append(keywords[i])
                else:
                    print('Error: ' + str(page.status_code))

        if (isRaw):
            self.OutputRaw()
        else:
            self.OutputCSV()

    
    def OutputCSV(self):
        with open('out/surrey.csv', 'w', newline='', encoding='utf-8') as csvFile:
            headerList = ['Title', 'Href', 'Author', 'Date', 'Abstract', 'Keywords', 'University Name']
            writer = csv.DictWriter(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, fieldnames=headerList)
            writer.writeheader()
            for x in range(len(self.titleArr)):
                writer.writerow({'Title': self.titleArr[x], 'Href': self.hrefArr[x], 'Author': self.authorArr[x], 'Date': self.dateArr[x], 'Abstract': self.abstractArr[x], 'Keywords': self.keywordsArr[x], 'University Name': 'University of Manchester'})

    def OutputRaw(self):
        print('Title,Href,Author,Date,Abstract,Keyword,University Name')
        for x in range(len(self.arr)):
            print(self.titleArr[x] + ',' + self.hrefArr[x] + ',' + self.authorArr[x] + ',' + self.dateArr[x] + ',' + self.abstractArr[x] + ',' + self.keywordsArr[x] + 'University of Manchester')


    def GetAuthors(self, span):
        para = span.find('p', {'class': 'authors'})
        authorSpans = para.find_all('span')
        output = ''
        for x in range(len(authorSpans)):
            if x == 0:
                output = authorSpans[x].get_text()
            else:
                output = output + '; ' + authorSpans[x].get_text()

        return output


    def GetAbstract(self, span):
        body = span.find('div', {'class': 'content'})
        if body == None:
            return 'None'

        return body.get_text()


    def GetDate(self, span):
        paras = span.find_all('p')
        date = paras[5].get_text()
        return date