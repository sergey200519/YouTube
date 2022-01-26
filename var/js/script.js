let btn = document.querySelector(".btn")

let flag = true
function variable(status) {
  if (status) {
    document.documentElement.style.setProperty("--background", "black")
    document.documentElement.style.setProperty("--color-text", "black")
    document.documentElement.style.setProperty("--box-background", "white")
    flag = false
  } else {
    document.documentElement.style.setProperty("--background", "white")
    document.documentElement.style.setProperty("--color-text", "white")
    document.documentElement.style.setProperty("--box-background", "black")
    flag = true
  }
}

btn.addEventListener("click", function (e) {
  variable(flag)
});
