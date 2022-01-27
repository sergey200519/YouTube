let key = document.querySelector(".key")
let data = document.querySelector(".data")
let area = document.querySelector(".from_local_storage")
let addBtn = document.querySelector(".add")
let watchBtn = document.querySelector(".watch")
let watchAllBtn = document.querySelector(".watch_all")
let removeBtn = document.querySelector(".remove")
let clearBtn = document.querySelector(".clear")

addBtn.addEventListener("click", function (e) {
  localStorage.setItem(key.value, data.value)
})

watchBtn.addEventListener("click", function (e) {
  area.value = localStorage.getItem(key.value)
})

watchAllBtn.addEventListener("click", function (e) {
  let answer = ""
  for (let i = 0; i < localStorage.length; i++){
      answer += localStorage.key(i) + " : " + localStorage.getItem(localStorage.key(i)) + "\n"
  }
  area.value = answer
})

removeBtn.addEventListener("click", function (e) {
  localStorage.removeItem(key.value)
})

clearBtn.addEventListener("click", function (e) {
  localStorage.clear()
})




// let obj = {
//   name: "Tom",
//   age: 25
// }
//
// localStorage.setItem("user", JSON.stringify(obj))
// console.log(typeof localStorage.getItem("user"));
// console.log(typeof JSON.parse(localStorage.getItem("user")));


window.addEventListener("storage", function (e) {
  console.log(e);
})


















//
