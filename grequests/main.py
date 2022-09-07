import grequests
import requests
import json
from bs4 import BeautifulSoup

my_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
base_url = "https://spravochnik-ru.com/1-moskva/"
urls = []
i = 1
n = 100
while i <= n:
    urls.append(f"{base_url}{i}")
    i += 1
print("urls собраны")


def exception_handler(request, exception):
    print(f"ERROR {request.url}\n{exception}")


response = (grequests.get(url, headers=my_headers) for url in urls)
results = grequests.imap(response, exception_handler=exception_handler)
print("запросы сделаны")

phone_dict = {}
for res in results:
    if res.status_code == 200:
        print("обработка кодa")
        html = res.text
        soup = BeautifulSoup(html, "lxml")
        tr = soup.select("table[class='table table-bordered table-striped'] > tbody > tr")
        for item in tr:
            td = item.select("td")
            name = td[1].select_one("a").text.strip()
            phone_number = td[2].text.strip()
            address = td[3].text.strip()
            url = f"https://spravochnik-ru.com{td[1].select_one('a')['href']}"
            phone_dict[name] = {
                "phone": phone_number,
                "address": address,
                "url": url
            }

with open("phone_number.json", "w", encoding="utf-8") as file:
    json.dump(phone_dict, file, indent=4, ensure_ascii=False)
