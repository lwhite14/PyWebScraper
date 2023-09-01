from .University import University
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import csv
from dateutil.parser import parse

class Lancaster(University):
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
                url = 'https://www.research.lancs.ac.uk/portal/en/publications/search.html?publicationYearsFrom=&publicationstatus=&advanced=true&documents=%20&language=%20&publicationYearsTo=&type=%20&uri=&search='+keywords[i]+'&organisationName=&organisations=&publicationcategory=&peerreview=&pageSize=25&page='+str(y)
                page = requests.get(url)

                if page.status_code == 200:
                    soup = BeautifulSoup(page.text, "html.parser")
                    lis = soup.find_all("li", {"class": "portal_list_item"})

                    for x in tqdm(range(len(lis)), ncols=80, ascii=True, desc=keywords[i] + "; Page " + str(1 + y)):
                        self.titleArr.append(lis[x].find("h2", {"class": "title"}).get_text())
                        href = lis[x].find("h2", {"class": "title"}).find("a").get("href")
                        self.hrefArr.append(href)
                        self.authorArr.append(self.GetAuthors(lis[x]))
                        self.dateArr.append(lis[x].find("span", {"class": "date"}).get_text())
                        self.abstractArr.append(self.GetAbstract(href))
                        self.keywordsArr.append(keywords[i])
                else:
                    print("Error: " + str(page.status_code))

        if (isRaw):
            self.OutputRaw()
        else:
            self.OutputCSV()


    def OutputCSV(self):
        with open('out/lancaster.csv', 'w', newline='', encoding='utf-8') as csvFile:
            headerList = ['Title', 'Href', 'Author', 'Date', 'Abstract', 'Keywords', 'University Name']
            writer = csv.DictWriter(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, fieldnames=headerList)
            writer.writeheader()
            for x in range(len(self.titleArr)):
                writer.writerow({'Title': self.titleArr[x], 'Href': self.hrefArr[x], 'Author': self.authorArr[x], 'Date': self.dateArr[x], 'Abstract': self.abstractArr[x], 'Keywords': self.keywordsArr[x], 'University Name': 'University of Lancaster'})

    def OutputRaw(self):
        print("Title,Href,Author,Date,Abstract,Keyword,University Name")
        for x in range(len(self.arr)):
            print(self.titleArr[x] + ',' + self.hrefArr[x] + ',' + self.authorArr[x] + ',' + self.dateArr[x] + ',' + self.abstractArr[x] + ',' + self.keywordsArr[x] + 'University of Lancaster')


    def GetAuthors(self, li):
        persons = li.find_all("a", {"class": "link person"})
        output = ''
        for x in range(len(persons)):
            if x == 0:
                output = persons[x].find("span").get_text()
            else:
                output = output + '; ' + persons[x].find("span").get_text()
        return output

    def GetAbstract(self, href):
        page = requests.get(href)
        soup = BeautifulSoup(page.text, "html.parser")
        div = soup.find("div", {"class": "view_container publication_view"})

        divSpec = soup.find("div", {"class": "textblock"})
        if divSpec != None:
            p = divSpec.find("p")
            if p != None:
                return p.get_text()
            else:
                return divSpec.get_text()

        return "None"