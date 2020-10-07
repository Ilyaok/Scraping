from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://hays.ru/search/")

for i in range(5):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(3)

VacHeads = []
for temp in driver.find_elements_by_tag_name("h3"):
    VacHeads.append(temp.text)

Industries = []
for temp in driver.find_elements_by_class_name("svc-search-results__position"):
    Industries.append(temp.find_element_by_tag_name("p").text)

Locations = []
for temp in driver.find_elements_by_class_name("locations-labl"):
    Locations.append(temp.find_element_by_tag_name("span").text)

table = {"Vacancy": VacHeads, "Industry": Industries, "Location": Locations}
frame = pd.DataFrame(table)

writer = pd.ExcelWriter("Hays_Vacancies.xlsx", engine='xlsxwriter')
frame.to_excel(writer, "Vacancies")
writer.save()

driver.close()