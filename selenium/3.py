from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time
import json
import pickle


with open("avito.json", "r", encoding="utf-8") as f:
    avito = json.loads(f.read())


opt = webdriver.ChromeOptions()
opt.add_argument("--disable-blink-features=AutomationControlled")
opt.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)


try:
    browser.get("https://www.avito.ru/#login?authsrc=h")
    time.sleep(1)
    login = browser.find_element(By.NAME, 'login')
    login.clear()
    login.send_keys(avito["login"])
    time.sleep(1)
    password = browser.find_element(By.NAME, "password")
    password.clear()
    password.send_keys(avito["password"])
    password.send_keys(Keys.ENTER)
    time.sleep(30)
    pickle.dump(browser.get_cookies(), open("avito_cookies", "wb"))
    time.sleep(5)
except Exception:
    print("Error")
finally:
    browser.close()
    browser.quit()





#
