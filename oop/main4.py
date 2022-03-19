class Number:
    __slots__ = ("num")

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Number(self.num + other.num)

    def __str__(self):
        return str(self.num)



a = Number(5)
print(a)
a.num = 8
a.test = 1
print(a)
