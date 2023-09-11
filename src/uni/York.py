from .University import University
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import csv
from dateutil.parser import parse

class York(University):
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
                url = 'https://eprints.whiterose.ac.uk/cgi/search/archive/advanced?exp=0%7C1%7C-date%2Fcreators_name%2Ftitle%7Carchive%7C-%7Ciau%3Aiau%3AANY%3AEQ%3AYork%7Ckeywords%3Akeywords%3AALL%3AIN%3A'+keywords[i]+'%7C-%7Ceprint_status%3Aeprint_status%3AANY%3AEQ%3Aarchive%7Cmetadata_visibility%3Ametadata_visibility%3AANY%3AEQ%3Ashow&_action_search=1&order=-date%2Fcreators_name%2Ftitle&screen=Search&cache=16777394&search_offset='+str(y*2)+'0'
                page = requests.get(url)

                if page.status_code == 200:
                    soup = BeautifulSoup(page.text, "html.parser")
                    trs = soup.find_all("tr", {"class": "ep_search_result"})

                    for x in tqdm(range(len(trs)), ncols=80, ascii=True, desc=keywords[i] + "; Page " + str(1 + y)):
                        self.titleArr.append(trs[x].find("em").get_text())
                        href = self.GetHref(trs[x])
                        self.hrefArr.append(href)
                        self.authorArr.append(self.GetAuthors(trs[x]))
                        self.dateArr.append(self.GetDate(href).strftime("%B %Y"))
                        self.abstractArr.append(self.GetAbstract(href))
                        self.keywordsArr.append(keywords[i])
                else:
                    print("Error: " + str(page.status_code))

        if (isRaw):
            self.OutputRaw()
        else:
            self.OutputCSV()


    def OutputCSV(self):
        with open('out/york.csv', 'w', newline='', encoding='utf-8') as csvFile:
            headerList = ['Title', 'Href', 'Author', 'Date', 'Abstract', 'Keywords', 'University Name']
            writer = csv.DictWriter(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, fieldnames=headerList)
            writer.writeheader()
            for x in range(len(self.titleArr)):
                writer.writerow({'Title': self.titleArr[x], 'Href': self.hrefArr[x], 'Author': self.authorArr[x], 'Date': self.dateArr[x], 'Abstract': self.abstractArr[x], 'Keywords': self.keywordsArr[x], 'University Name': 'University of York'})

    def OutputRaw(self):
        print("Title,Href,Author,Date,Abstract,Keyword,University Name")
        for x in range(len(self.arr)):
            print(self.titleArr[x] + ',' + self.hrefArr[x] + ',' + self.authorArr[x] + ',' + self.dateArr[x] + ',' + self.abstractArr[x] + ',' + self.keywordsArr[x] + 'University of York')


    def GetAuthors(self, tr):
        authorSpans = tr.find_all('span', {'class':'person_name'})
        if authorSpans != None:
            output = ''
            for x in range(len(authorSpans)):
                if x == 0:
                    output = authorSpans[x].get_text()
                else:
                    output = output + '; ' + authorSpans[x].get_text()
            return output
        else:
            return "None"


    def GetHref(self, tr):
        hrefs = tr.find_all('a', {'class': None})
        if len(hrefs) == 1:
            return hrefs[0].get("href")
        else:
            return "None"


    def GetDate(self, href):
        page = requests.get(href)
        soup = BeautifulSoup(page.text, "html.parser")

        ul = soup.find("ul", {"class": "datesdatesdates"})
        
        lis = ul.find_all("li")
        dates = []

        for li in lis:
            dates.append(parse(li.get_text(), fuzzy=True))

        return dates[0]


    def GetAbstract(self, href):
        page = requests.get(href)
        soup = BeautifulSoup(page.text, "html.parser")
        pAbstract = soup.find("p", {"class": "abstract"})
        if pAbstract != None:
            return pAbstract.get_text()
        else:
            return "None"