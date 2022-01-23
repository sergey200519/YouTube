let btn = document.querySelector(".btn")
let link = document.querySelector(".theme")

let flag = true
function theme(status) {
  if (status) {
    link.href = "style/dark.css"
    flag = false
  } else {
    link.href = "style/style.css"
    flag = true
  }
}

btn.addEventListener("click", function (e) {
  theme(flag)
});
console.log(new Date());
function time() {
  let time = new Date();
  console.log(time.getHours(), ":", time.getMinutes());
}
setInterval(time, 60 * 100)
