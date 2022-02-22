// function calc(a, b) {
//   return [
//     a % b,
//     undefined,
//     Math.abs(a),
//     Math.abs(b)
//   ]
// }

// let result = calc(5, -6)
// let rest = result[0]
// let exp = result[1]
// let one_module = result[2]
// let two_module = result[3]
//
// console.log(result, exp, one_module, two_module)



//
// let [rest, exp = 0, ...other] = calc(5, -6)
// console.log(rest, exp, other)




const user = {
  name: "Sergey",
  age: 16,
  contry: "Russia",
  data: {
    id: 45,
    log: "Sergey12345"
  }
}

// const userName = user.name
// const age = user.age


const {name: userName,
age = 0,
...other
} = user
console.log(userName, age, other);


















//
