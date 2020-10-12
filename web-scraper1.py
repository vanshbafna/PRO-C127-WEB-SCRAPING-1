import requests
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://www.windows2universe.org/our_solar_system/moons_table.html"
headers = ["name", "year_discovered", "discoverer", "distance_from_planet (km)", "diameter (km)", "orbital_period", "host_planet"]
moons_data = []
page = requests.get(START_URL, verify=False)

###
soup = BeautifulSoup(page.content, "html.parser")
tables = soup.find_all("table", attrs={"border": "5"})
table = tables[1]
tr = table.find_all("tr", attrs={"align": "center", "valign": "center"})[0]
temp_list = []
for index, td_tag in enumerate(tr.find_all("td")):
    if index == 0:
        try:
            temp_list.append(
                td_tag.find_all("a")[0].contents[0]
            )
        except:
            try:
                temp_list.append(td_tag.find_all("strong")[0].contents[0])
            except:
                temp_list.append(td_tag.contents[0])
    else:
        temp_list.append(td_tag.contents[0])
moons_data.append(temp_list)

with open("main.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(moons_data)
