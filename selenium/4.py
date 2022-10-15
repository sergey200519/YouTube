from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time
import pickle

opt = webdriver.ChromeOptions()
opt.add_argument("--disable-blink-features=AutomationControlled")
opt.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)


try:
    browser.get("https://www.avito.ru/")
    time.sleep(1)
    cookies = pickle.load(open("avito_cookies", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.refresh()

    time.sleep(10)
except Exception:
    print("Error")
finally:
    browser.close()
    browser.quit()





#
