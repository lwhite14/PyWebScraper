from .University import University
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import csv

class UWE(University):
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
            url = "https://uwe-repository.worktribe.com/search/all/outputs?criteria=" + keywords[i]
            page = requests.get(url)

            if page.status_code == 200:
                soup = BeautifulSoup(page.text, "html.parser")
                divs = soup.find_all("blockquote")

                amountOfMaterial = depth * 25
                if len(divs) < amountOfMaterial:
                    amountOfMaterial = len(divs)

                for x in tqdm(range(amountOfMaterial), ncols=80, ascii=True, desc=keywords[i]):
                    self.titleArr.append(divs[x].find("strong").get_text())
                    href = divs[x].find("a").get("href")
                    self.hrefArr.append(href)
                    researchPage = requests.get(href)
                    self.authorArr.append(self.GetAuthors(researchPage))
                    self.dateArr.append(self.GetDate(researchPage))
                    self.abstractArr.append(self.GetAbstract(researchPage))
                    self.keywordsArr.append(keywords[i])
            else:
                print("Error: " + str(page.status_code))

        if (isRaw):
            self.OutputRaw()
        else:
            self.OutputCSV()


    def OutputCSV(self):
        with open('out/uwe.csv', 'w', newline='', encoding='utf-8') as csvFile:
            headerList = ['Title', 'Href', 'Author', 'Date', 'Abstract', 'Keywords', 'University Name']
            writer = csv.DictWriter(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, fieldnames=headerList)
            writer.writeheader()
            for x in range(len(self.titleArr)):
                writer.writerow({'Title': self.titleArr[x], 'Href': self.hrefArr[x], 'Author': self.authorArr[x], 'Date': self.dateArr[x], 'Abstract': self.abstractArr[x], 'Keywords': self.keywordsArr[x], 'University Name': 'University of the West of England'})

    def OutputRaw(self):
        print("Title,Href,Author,Date,Abstract,Keyword,University Name")
        for x in range(len(self.arr)):
            print(self.titleArr[x] + ',' + self.hrefArr[x] + ',' + self.authorArr[x] + ',' + self.dateArr[x] + ',' + self.abstractArr[x] + ',' + self.keywordsArr[x] + 'University of the West of England')


    def GetAuthors(self, researchPage):
        if researchPage.status_code == 200:
            soup = BeautifulSoup(researchPage.text, "html.parser")
            output = ""

            divs = soup.find("div", {"style": "max-height: 100vh; overflow: auto;"})
            strongs = []
            if divs != None:
                strongs = divs.find_all("strong")

            for i in range(len(strongs)):
                if i != 0:
                    output += "; " + strongs[i].get_text()
                else:
                    output += strongs[i].get_text()

            if output == "":
                return "None"
            return output
        else:
            return "None";
    
    def GetDate(self, researchPage):
        if researchPage.status_code == 200:
            soup = BeautifulSoup(researchPage.text, "html.parser")
            output = "None"

            trs = soup.find_all("tr")

            for i in range(len(trs)):
                if trs[i].find("th").get_text() == "Publication Date":
                    output = trs[i].find("td").get_text()
                    break

            return output
        else:
            return "None";
    
    def GetAbstract(self, researchPage):
        if researchPage.status_code == 200:
            soup = BeautifulSoup(researchPage.text, "html.parser")
            output = "None"
            div = soup.find("div", {"class": "content abstract"})
            if div != None:
                output = div.find("p").get_text()
            return output
        else:
            return "None";