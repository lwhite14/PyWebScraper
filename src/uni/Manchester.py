from .University import University
from bs4 import BeautifulSoup
import requests

class Manchester(University):
    arr = []

    def __init__(self):
        pass


    def ScrapeForData(self, isRaw):
        url = 'https://research.manchester.ac.uk/en/publications/'
        page = requests.get(url)

        if page.status_code == 200:
            soup = BeautifulSoup(page.text, "html.parser")
            divs = soup.find_all("div", {"class": "result-container"})

            titleArr = []
            hrefArr = []
            authorArr = []
            dateArr = []
            abstractArr = []
            keywordsArr = []

            for div in divs:
                titleArr.append(div.find("h3").get_text())
                hrefArr.append(div.find("a").get("href"))
                authorArr.append(self.GetAuthors(div))
                dateArr.append(div.find("span", {"class": "date"}).get_text())
                abstractArr.append(" ")
                keywordsArr.append(" ")

            for x in range(len(divs)):
                self.arr.append(titleArr[x] + "_" + hrefArr[x] + "_" + authorArr[x] + "_" + dateArr[x] + "_" + abstractArr[x] + "_" + keywordsArr[x] + "_" + "University of Manchester")

            if (isRaw):
                self.OutputRaw()
            else:
                self.OutputCSV()

        else:
            print("Error: " + str(page.status_code))


    def OutputCSV(self):
        f = open("out/manchester.csv", "w")
        f.write("Title_Href_Author_Date_Abstract_Keyword_University Name\n")
        for x in range(len(self.arr)):
            f.write(self.arr[x] + "\n")
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