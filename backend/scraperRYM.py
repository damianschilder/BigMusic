#mandatory to use chrome https://www.youtube.com/watch?v=j7VZsCCnptM, https://chromedriver.chromium.org/home, https://stackoverflow.com/questions/51213150/selenium-python-wait-doesnt-work
#pip install beautifulsoup4, lxml, selenium

#from bs4 import BeautifulSoup
#import requests


import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import re
options = Options()
options.headless = True #True/False for hidden chrome
options.add_argument("--window-size=1920,1500")

os.environ["PATH"] += r"/Drivers_Selenium"
DRIVER_PATH = "/Drivers_Selenium"
rymInput=input("Which artist?")
rymInput= str(rymInput)
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options= options)
driver.get("https://rateyourmusic.com/search?searchterm="+ rymInput +"&searchtype=")


#element1 = driver.find_element(By.ID, "onetrust-reject-all-handler")

#time.sleep(10)
#artists=wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[4]/div[3]/div[2]/ul/li[1]/div[1]/a")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".fc-cta-consent > p:nth-child(2)"))).click()  #accept cookies
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".page_search_results > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > b:nth-child(1) > a:nth-child(1)"))).click()  #click on first result

rymName= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[1]/div/div[7]/div[1]/div[1]/div/div[1]/div[2]/h1"))).text   #title/name
rymDescr= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[1]/div/div[7]/div[1]/div[1]/div/div[3]/div[2]/div[1]/div[2]"))).text   #description
rymName = re.sub("[\(\[].*?[\)\]]", "", rymName)    #remove unwanted text
rymDescr = re.sub("[\(\[].*?[\)\]]", "", rymDescr)
#rymDescr= driver.find_element((By.CSS_SELECTOR, "div.content:nth-child(2)"))
#print(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div[2]/div[1]/div[1]/div/div[3]/div/div[2]"))).get_attribute("outerHTML"))
#print(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "html.is_not_mobile.needs_reduced_ui.haslocalstorage.no_hastouch.no_indevmode.no_ismobile.hasformdata.hashistoryapi.hasflexbox body.win.firefox.firefox107 div#main_wrapper div#page.aside_off_canvas div#page_content div.lr.group div.left div.body.artist-header-container div.artist-profile div.profile div.content div#profile.readmore.initialized")))).text
print(rymName)
print(rymDescr)

driver.quit()
#artists = driver.find_element(By.CSS_SELECTOR, "li.card:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
#artists = driver.find_element(By.ID, By.XPATH, "/html/body/div[1]/div[4]/div[3]/div[2]/ul/li[1]/div[1]/a") search_result_title
#element1.click()
#artists.click()

#for artist in artists:
#    artist=



#driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
#driver.get("https://www.discogs.com/search/?q=rammstein&type=artist")
#print(driver.page_source)
#driver.quit()

#Scraper met bs4 werkt niet door cloudflare
#htmlTxt = requests.get("https://www.discogs.com/search/?q=rammstein&type=artist").text
#print(htmlTxt)