from selenium import webdriver
import pandas as pd


driver = webdriver.Chrome()
driver.get("https://ru.globalcareer.eu/candidates/")

VacHeads = []
for temp in driver.find_elements_by_class_name("name"):
    VacHeads.append(temp.text)

Locations = []
for temp in driver.find_elements_by_class_name("location"):
    if temp.text == '':
        Locations.append("No data")
    else:
        Locations.append(temp.text)

Dates = []
for temp in driver.find_elements_by_class_name("job-date"):
        Dates.append(temp.text)

table = {"Vacancy": VacHeads, "Location": Locations, "Date of creation": Dates}
frame = pd.DataFrame(table)

writer = pd.ExcelWriter("GC_Vacancies2.xlsx", engine='xlsxwriter')
frame.to_excel(writer, "Vacancies")
writer.save()

driver.close()







