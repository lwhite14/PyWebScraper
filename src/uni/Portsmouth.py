from .University import University
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import csv

class Portsmouth(University):
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
                url = "https://researchportal.port.ac.uk/en/searchAll/advanced/?searchByRadioGroup=PartOfNameOrTitle&searchBy=PartOfNameOrTitle&allThese=" + keywords[i] + "&exactPhrase=&or=&minus=&family=publications&doSearch=Search&slowScroll=true&resultFamilyTabToSelect=&page=" + str(y)
                page = requests.get(url)

                if page.status_code == 200:
                    soup = BeautifulSoup(page.text, "html.parser")
                    divs = soup.find_all("div", {"class": "result-container"})

                    for x in tqdm(range(len(divs)), ncols=80, ascii=True, desc=keywords[i] + "; Page " + str(1 + y)):
                        if not x == 0:
                            self.titleArr.append(divs[x].find("h3").get_text())
                            href = divs[x].find("a").get("href")
                            self.hrefArr.append(href)
                            self.authorArr.append(self.GetAuthors(divs[x]))
                            self.dateArr.append(divs[x].find("span", {"class": "date"}).get_text())
                            self.abstractArr.append(self.GetAbstract(href))
                            self.keywordsArr.append(keywords[i])
                else:
                    print("Error: " + str(page.status_code))

        if (isRaw):
            self.OutputRaw()
        else:
            self.OutputCSV()


    def OutputCSV(self):
        with open('out/portsmouth.csv', 'w', newline='', encoding='utf-8') as csvFile:
            headerList = ['Title', 'Href', 'Author', 'Date', 'Abstract', 'Keywords', 'University Name']
            writer = csv.DictWriter(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, fieldnames=headerList)
            writer.writeheader()
            for x in range(len(self.titleArr)):
                writer.writerow({'Title': self.titleArr[x], 'Href': self.hrefArr[x], 'Author': self.authorArr[x], 'Date': self.dateArr[x], 'Abstract': self.abstractArr[x], 'Keywords': self.keywordsArr[x], 'University Name': 'University of Manchester'})

    def OutputRaw(self):
        print("Title,Href,Author,Date,Abstract,Keyword,University Name")
        for x in range(len(self.arr)):
            print(self.titleArr[x] + ',' + self.hrefArr[x] + ',' + self.authorArr[x] + ',' + self.dateArr[x] + ',' + self.abstractArr[x] + ',' + self.keywordsArr[x] + 'University of Manchester')

    def GetAuthors(self, currentDiv):
        authorString = ""
        spans = currentDiv.find_all("span")
        for x in range(len(spans)):
            if x != 0:
                if spans[x].get("class") == ['date']:
                    break;
                if spans[x].get("class") == None:
                    if x != 1:
                        authorString += "; " + spans[x].get_text()
                    else:
                        authorString += spans[x].get_text()

        return authorString


    def GetAbstract(self, href):
        page = requests.get(href)
        soup = BeautifulSoup(page.text, "html.parser")

        abstractDiv = soup.find("div", {"class": "textblock"})
        if abstractDiv == None:
            return "None"
        
        return abstractDiv.get_text()