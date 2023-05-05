from .University import University
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

class Manchester(University):
    arr = []

    def __init__(self):
        pass


    def ScrapeForData(self, isRaw, depth, keywords):
        for i in range(depth):
            url = "https://research.manchester.ac.uk/en/searchAll/advanced/?searchByRadioGroup=PartOfNameOrTitle&searchBy=PartOfNameOrTitle&allThese=" + keywords + "&exactPhrase=&or=&minus=&family=publications&doSearch=Search&slowScroll=true&resultFamilyTabToSelect=&page=" + str(i)
            page = requests.get(url)

            titleArr = []
            hrefArr = []
            authorArr = []
            dateArr = []
            abstractArr = []
            keywordsArr = []

            if page.status_code == 200:
                soup = BeautifulSoup(page.text, "html.parser")
                divs = soup.find_all("div", {"class": "result-container"})

                print("Parsing page "+ str(i + 1) + "...")
                for x in tqdm(range(len(divs))):
                    if not x == 0:
                        titleArr.append(divs[x].find("h3").get_text())
                        href = divs[x].find("a").get("href")
                        hrefArr.append(href)
                        authorArr.append(self.GetAuthors(divs[x]))
                        dateArr.append(divs[x].find("span", {"class": "date"}).get_text())
                        abstractArr.append(self.GetAbstract(href))
                        keywordsArr.append(keywords)

                for x in range(len(divs) - 1):
                    self.arr.append(self.wrap + titleArr[x] + self.wrap + self.sep + self.wrap + hrefArr[x] + self.wrap + self.sep + self.wrap + authorArr[x] + self.wrap + self.sep + self.wrap + dateArr[x] + self.wrap + self.sep + self.wrap + abstractArr[x] + self.wrap + self.sep + self.wrap + keywordsArr[x] + self.wrap + self.sep + self.wrap + "University of Manchester\"")

            else:
                print("Error: " + str(page.status_code))

        if (isRaw):
            self.OutputRaw()
        else:
            self.OutputCSV()


    def OutputCSV(self):
        f = open("out/manchester.csv", "w", encoding="utf-8")
        f.write("Title_Href_Author_Date_Abstract_Keyword_University Name" + u"\n")
        for x in range(len(self.arr)):
            f.write(self.arr[x] + u"\n")
        f.close()


    def OutputRaw(self):
        print("Title_Href_Author_Date_Abstract_Keyword_University Name")
        for x in range(len(self.arr)):
            print(self.arr[x])


    def GetAuthors(self, currentDiv):
        # Getting the authors is a bit more complicated
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