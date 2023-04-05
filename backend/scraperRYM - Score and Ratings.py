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

driver = webdriver.Chrome(executable_path=DRIVER_PATH, options= options)
driver.get("https://rateyourmusic.com/release/album/portishead/dummy/")

rymScore= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[8]/div[2]/div/div[1]/div[1]/div/table[2]/tbody/tr/td[1]/table/tbody/tr[5]/td/span/span[1]"))).text   #title/name
rymRatings= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div/div/div[8]/div[2]/div/div[1]/div[1]/div/table[2]/tbody/tr/td[1]/table/tbody/tr[5]/td/span/span[3]/b/span"))).text   #description
rymScore = re.sub("[\(\[].*?[\)\]]", "", rymScore)    #remove unwanted text
rymRatings = re.sub("[\(\[].*?[\)\]]", "", rymRatings)

print(rymScore)
print(rymRatings)

driver.quit()
