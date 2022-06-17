class User {
  #password;
  #basket = []
  logined = false
  constructor(userName, age, userEmail, password) {
    this.name = userName
    this.age = age
    this._email = userEmail
    this.#password = password
    if (this.isAdult()) {
      this.#login()
    }
  }

  isAdult() {
    return this.age >= 18 ? true : false
  }

  addBasket(item) {
    if (this.logined) {
      this.#basket.push(item)
    } else {
      console.log("Пользователь не залогирован");
    }
  }

  #login() {
    this.logined = true
  }

  get password() {
    return this.#password
  }

  get baskets() {
    return this.#basket
  }

  set password(password) {
    if (password != "") {
      this.#password = password
    }
  }
}

// const user = new User("sergey", 19, "email@mail.ru", "12345")
// console.log(user)

// -------------------------------------------------------------------

// function fun() {
//   return class {
//     #password
//     constructor(userName, age, userEmail, password) {
//       this.name = userName
//       this.age = age
//       this._email = userEmail
//       this.#password = password
//     }
//   }
// }

class Admin extends User {
  constructor(adminName, age, adminEmail, password, post) {
    super(adminName, age, adminEmail, password)
    this.post = post
  }

  createUser(userName, age, userEmail, password) {
    let user = new User(userName, age, userEmail, password)
    console.log(user)
  }

  // isAdult() {
  //   if (super.isAdult()) {
  //     return "возраст для работы подходит"
  //   }
  //   return  "возраст для работы не подходит"
  // }

  addBasket(item) {
    console.log("у админа нет корзины")
  }

  get baskets() {
    return "нет корзины"
  }
}

const admin = new Admin("max", 30, "max@mail.ru", "max123", "junior admin")
console.log(admin)
admin.createUser("alexey", 23, "alexey@mail.ru", "alexey23")
//console.log(admin.isAdult())
admin.addBasket()
console.log(admin.baskets)





































// function getParentData() {
//   return super.isAdult()
// }
// return getParentData() + " возраст"
// return setTimeout(() => {console.log(super.isAdult())}, 0)
//
