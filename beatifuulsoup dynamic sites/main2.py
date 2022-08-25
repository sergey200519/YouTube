import requests
import json


my_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
i = 1
n = 1
while i <= n:
    url = f"https://www.landingfolio.com/api/inspiration?page={i}&sortBy=free-first"
    req = requests.get(url, headers=my_headers)
    data = json.loads(req.text)
    i += 1
