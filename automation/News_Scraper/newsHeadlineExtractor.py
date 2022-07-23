from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()
# MMDDYYYY
month_day_year = now.strftime("%m%d%Y")


website = "https://www.thesun.co.uk/sports/football/"
path = "./chromedriver/chromedriver.exe"

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')

option = Options()
option.headless = True
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=option)

driver.get(website)

containers = driver.find_elements(
    by="xpath", value='//div[@class="teaser__copy-container"]')

# print(containers)

titles = []
subtitles = []
links = []


for container in containers:
    title = container.find_element(
        by="xpath", value='./a/h2').text

    subtitle = container.find_element(
        by="xpath", value='./a/p').text
    link = container.find_element(
        by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)


# Exporting data to a CSV file
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)

file_name = f'headline--{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
print(final_path)
df_headlines.to_csv(final_path)

driver.quit()
