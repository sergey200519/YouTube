import requests


my_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
url = "https://spravochnik-ru.com/1-moskva"
req = requests.get(url, headers=my_headers)
html = req.text
print(html)
print(req.status_code)
print(req.url)



































from bs4 import BeautifulSoup

# my_headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
# }
# url = "https://spravochnik-ru.com/1-moskva"
# req = requests.get(url, headers=my_headers)
# html = req.text
# soup = BeautifulSoup(html, "lxml")
# print(f"find ---> {soup.find('h1').text}")
# print(f"select_one ---> {soup.select_one('h1.text-center').text}")# "h1[class='text-center']"
# print(f"select ---> {soup.select('p')}")












# import json
# base_url = "https://spravochnik-ru.com/1-moskva/"
# result = {}
# n = 10
# i = 1
# while i <= n:
#     url = f"{base_url}{i}"
#     req = requests.get(url)
#     if req.status_code == 200:
#         html = req.text
#         soup = BeautifulSoup(html, "lxml")
#         tr = soup.select("table[class='table table-bordered table-striped'] > tbody > tr")
#         for item in tr:
#             td = item.select("td")
#             name = td[1].select_one("a").text.strip()
#             phone_number = td[2].text.strip()
#             address = td[3].text.strip()
#             url = f"https://spravochnik-ru.com{td[1].select_one('a')['href']}"
#             result[name] = {
#                 "phone": phone_number,
#                 "address": address,
#                 "url": url
#             }
#     print(f"процес завершон на {i*100/n}% сейчас {i} итерация из {n}")
#     i += 1
#
# with open("phone_number.json", "w", encoding="utf-8") as file:
#     json.dump(result, file, indent=4, ensure_ascii=False)
