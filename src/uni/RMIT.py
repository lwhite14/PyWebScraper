from .University import University
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver 
from dateutil.parser import parse
import csv
import time

class RMIT(University):

    def ScrapeForData(self, isRaw, depth, keywords):
        print("The scraping for this University uses Selenium and will take longer to parse... You have been warned!")
        for i in range(len(keywords)):
            for y in range(depth):
                url = 'https://researchrepository.rmit.edu.au/esploro/search/outputs?query=any,contains,' + keywords[i] + '&page=' + str(y + 1) + '&scope=Research'
                options = webdriver.FirefoxOptions() 
                options.headless = True 
                driver = webdriver.Firefox(options=options)
                driver.get(url)
                time.sleep(5)
                htmlSource = driver.page_source
                driver.close()

                soup = BeautifulSoup(htmlSource, 'html.parser')
                spans = soup.find_all('span', {'class': 'brief-body'})

                for x in tqdm(range(len(spans)), ncols=80, ascii=True, desc=keywords[i] + '; Page ' + str(1 + y)):
                    self.titleArr.append(spans[x].find('a', {'class': 'ng-star-inserted'}).get_text())
                    self.hrefArr.append("https://researchrepository.rmit.edu.au" + spans[x].find('a', {'class': 'ng-star-inserted'}).get('href'))
                    self.authorArr.append(self.GetAuthors(spans[x]))
                    self.dateArr.append(self.GetDate(spans[x]))
                    self.abstractArr.append(self.GetAbstract(spans[x]))
                    self.keywordsArr.append(keywords[i])

        if (isRaw):
            self.OutputRaw("Royal Melbourne Institute of Technology")
        else:
            self.OutputCSV("Royal Melbourne Institute of Technology", "rmit")


    def GetAuthors(self, span):
        para = span.find('p', {'class': 'authors'})
        if para != None:
            authorSpans = para.find_all('span')
            output = ''
            for x in range(len(authorSpans)):
                if x == 0:
                    output = authorSpans[x].get_text()
                else:
                    output = output + '; ' + authorSpans[x].get_text()

            return output
        else:
            return "None"


    def GetAbstract(self, span):
        body = span.find('div', {'class': 'content'})
        if body == None:
            return 'None'

        return body.get_text()


    def GetDate(self, span):
        paras = span.find_all('p')
        for x in range(len(paras)):
            if self.IsDate(paras[x].get_text()):
                return paras[x].get_text()
        return "None"

    def IsDate(self, inputString, fuzzy=False):
        try: 
            parse(inputString, fuzzy=fuzzy)
            return True
        except ValueError:
            return False
