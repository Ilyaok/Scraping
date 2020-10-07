from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()
url = "https://ru.globalcareer.eu/candidates/"

t = 1
VacHeads = []
Locations = []
Dates = []


def TableCreate(ClassName, ListOfElements, driver):
    for temp in driver.find_elements_by_class_name(ClassName):
        ListOfElements.append(temp.text)


while True:
    driver.get("https://ru.globalcareer.eu/candidates/?PAGEN_1=%s" % t)
    if t != 1 and driver.find_element_by_class_name("selected").text == "1":
        break
    TableCreate("name", VacHeads, driver)
    TableCreate("location", Locations, driver)
    TableCreate("job-date", Dates, driver)
    t = t + 1



table = {"Vacancy": VacHeads, "Location": Locations, "Date of creation": Dates}
frame = pd.DataFrame(table)

writer = pd.ExcelWriter("GC_Vacancies.xlsx", engine='xlsxwriter')
frame.to_excel(writer, "Vacancies")
writer.save()

driver.close()
