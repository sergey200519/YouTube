from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import time


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Hello_World")


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


try:
    browser.get("https://webbrowsertools.com/useragent/")
    time.sleep(10)
except Exception:
    print("Error")
finally:
    browser.close()
    browser.quit()
