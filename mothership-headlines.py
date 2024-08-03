# pip intall selenium, pandas
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

# py to exe: pip install pyinstaller
# pyinstaller --onefile mothership-headlines.py
applicationPath = os.path.dirname(sys.executable)

now = datetime.now()
monthDayYear = now.strftime("%m%d%Y")

website = "https://mothership.sg/category/news/"
path = r"C:\Users\Admin\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# headless-mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="ind-article "]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a/div/div[@class="header"]/h1').text
    subtitle = container.find_element(by="xpath", value='./a/div/div[@class="header"]/p').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

myDict = {'title':titles, 'subtitle':subtitles, 'link':links}
dfHeadlines = pd.DataFrame(myDict)
fileName = f'headline-{monthDayYear}.csv'
finalPath = os.path.join(applicationPath, fileName)
dfHeadlines.to_csv(finalPath)

driver.quit()