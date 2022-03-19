class User:
    def __init__(self, name, age, passwd):
        self.name = name
        self._age = age
        self.__password = passwd

    def legal_age(self):
        return self._age >= 18

    def __get_passwd(self):
        return self.__password

    @classmethod
    def get_data(cls):
        try:
            return cls.__get_passwd(cls)
        except:
            return "classmethod"

    @staticmethod
    def length(string):
        return len(string)

user = User("Sergey", 16, 123)

class Admin(User):
    def __init__(self, name, age, password, post):
        super().__init__(name, age, password)
        self.__post = post

    def work(self):
        return f"{self.name} working ({self.__post})"

    def legal_age(self):
        return self._age >= 21

    def test(self):
        return self._age

    length = property(doc='(!) Disallowed inherited')


admin = Admin("Max", 27, 286, "manager")
print(admin.legal_age())
print(admin.test())