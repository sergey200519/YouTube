from selenium import webdriver


import time

driver_path = "/Users/admin/Desktop/sel/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Hello_World")
browser = webdriver.Chrome(executable_path=driver_path)


try:
    browser.get("https://github.com/")
    time.sleep(3)
except Exception:
    print("Error")
finally:
    browser.close()
    browser.quit()





#
