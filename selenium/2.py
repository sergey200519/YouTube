from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time
import json

with open("github.json", "r", encoding="utf-8") as f:
    github = json.loads(f.read())

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


try:
    browser.get("https://github.com/login")
    time.sleep(3)
    email = browser.find_element(By.ID, "login_field")
    email.clear()
    email.send_keys(github["email"])
    time.sleep(3)
    password = browser.find_element(By.NAME, "password")
    password.clear()
    password.send_keys(github["password"])
    button = browser.find_element(By.NAME, "commit")
    button.click()
    time.sleep(5)
except Exception:
    print("Error")
finally:
    browser.close()
    browser.quit()





#
