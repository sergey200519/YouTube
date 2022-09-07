import json
from bs4 import BeautifulSoup
import requests
base_url = "https://spravochnik-ru.com/1-moskva/"
result = {}
n = 30
i = 1
while i <= n:
    url = f"{base_url}{i}"
    req = requests.get(url)
    if req.status_code == 200:
        html = req.text
        soup = BeautifulSoup(html, "lxml")
        tr = soup.select("table[class='table table-bordered table-striped'] > tbody > tr")
        for item in tr:
            td = item.select("td")
            name = td[1].select_one("a").text.strip()
            phone_number = td[2].text.strip()
            address = td[3].text.strip()
            url = f"https://spravochnik-ru.com{td[1].select_one('a')['href']}"
            result[name] = {
                "phone": phone_number,
                "address": address,
                "url": url
            }
    print(f"процес завершон на {i*100/n}% сейчас {i} итерация из {n}")
    i += 1


with open("phone_number.json", "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
