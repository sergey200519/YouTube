class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Number(self.num + other.num)

    def __str__(self):
        return str(self.num)


a = Number(5)
b = Number(5)
c = a + b
print(c.num, " sum")
print(c, " __str__")