import csv
from bs4 import BeautifulSoup


with open("shop.xml", "r", encoding="utf-8") as file:
    xml = file.read()


soup = BeautifulSoup(xml, "lxml")
shop_data = [
    ["название продукта", "цена", "фото"]
]
products = soup.select("product")
for product in products:
    row = []
    row.append(product.select_one("name").text)
    row.append(product.select_one("price").text)
    row.append(product.select_one("image").text)
    shop_data.append(row)

with open("csv/shop.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(shop_data)
