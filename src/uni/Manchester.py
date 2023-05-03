from .University import University
from bs4 import BeautifulSoup
import requests

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

                for x in range(len(divs)):
                    if not x == 0:
                        titleArr.append(divs[x].find("h3").get_text())
                        hrefArr.append(divs[x].find("a").get("href"))
                        authorArr.append(self.GetAuthors(divs[x]))
                        dateArr.append(divs[x].find("span", {"class": "date"}).get_text())
                        abstractArr.append(" ")
                        keywordsArr.append(keywords)

                for x in range(len(divs) - 1):
                    self.arr.append(titleArr[x] + "_" + hrefArr[x] + "_" + authorArr[x] + "_" + dateArr[x] + "_" + abstractArr[x] + "_" + keywordsArr[x] + "_" + "University of Manchester")

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