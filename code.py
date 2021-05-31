from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(URL)
time.sleep(5)

headers = ["V-MAG","NAME","BAYER-DESIGNATION","DISTANCE","SPECTRAL-CLASS","MASS","RADIUS","LUMINOCITY"]
stardata = []

soup = BeautifulSoup(browser.page_source,"html.parser")
for trtag in soup.find_all("tr",attrs={"class","exoplanet"}):
    trtags = trtag.find_all("td")
    templist=[]
    for index,trtag in enumerate(trtags):
        if(index==0):
            templist.append(trtag.find_all("a")[0].contents[0])
        else:
            try:
                templist.append(trtag.contents[0])
            except:
                templist.append("N/A")
    stardata.append(templist)

with open("data.csv","w") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(stardata)