from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
frame = pd.DataFrame({})

vacHeads = []
vacLocations = []
vacDates = []

def DataExtract(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html, features='lxml')

    global vacHeads
    global vacLocations
    global vacDates

    for vacHead in bsObj.findAll("div", {"class": "name"}):
        vacHeads.append(vacHead.get_text())

    for vacLocation in bsObj.findAll("div", {"class": "location"}):
        if vacLocation.get_text().strip() == '':
            vacLocations.append("N/D")
        else:
            vacLocations.append(vacLocation.get_text().strip())

    for vacDate in bsObj.findAll("div", {"class": "job-date"}):
        vacDates.append(vacDate.get_text())

for i in range(1, 19):
    url = "https://ru.globalcareer.eu/candidates/?PAGEN_1=" + str(i)
    DataExtract(url)

data = {"Vacancy": vacHeads, "Location": vacLocations, "Date of creation": vacDates}
frame = pd.DataFrame(data)


writer = pd.ExcelWriter("GCVacancies.xlsx", engine='xlsxwriter')
frame.to_excel(writer, "GCVacancies")
writer.save()