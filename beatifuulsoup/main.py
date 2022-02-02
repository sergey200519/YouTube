from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    code = f.read()

tree = BeautifulSoup(code, "lxml")


# h2 = tree.find_all("h2")
# print(h2)
# for item in h2:
#     print(item.text)

# parent = tree.find("h2", class_="two_secion-title").find_parent()
# print(parent)
# parents = tree.find("h2", class_="two_secion-title").find_parents("body")
# print(parents)


# find_next() find_previous()
next = tree.find("h2", class_="two_secion-title").find_next().find_next().find_previous()
print(next)
print(next.text)





































#
# elem = tree.find("h2", class_="two_secion-title").get("class")
# print(elem)
#
