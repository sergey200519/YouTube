class User:
    def __init__(self, name, age, passwd):
        self.name = name
        self._age = age
        self.__password = passwd


user = User("Sergey", 16, 123)
user.address = "Russia"
print(user.address)
