#mandatory to use chrome https://www.youtube.com/watch?v=j7VZsCCnptM, https://chromedriver.chromium.org/home
#pip install beautifulsoup4, lxml, selenium

from bs4 import BeautifulSoup
import requests

#cloudflare bs, er moet toch eerst een bot komen om door te klikken na zoekopdracht.

import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

os.environ["PATH"] += r"/Drivers_Selenium"
DRIVER_PATH = "/Drivers_Selenium"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://www.discogs.com/search/?q=rammstein&type=artist")
driver.implicitly_wait(2.358)
element = driver.find_element("class name","search_result_title")
element.click()

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.discogs.com/search/?q=rammstein&type=artist")
print(driver.page_source)
driver.quit()

#Scraper met bs4 werkt niet door cloudflare
#htmlTxt = requests.get("https://www.discogs.com/search/?q=rammstein&type=artist").text
#print(htmlTxt)