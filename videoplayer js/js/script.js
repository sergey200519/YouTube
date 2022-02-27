class Player {
  status = false
  statusZoom = false
  video; progress; play; speed; zoom; sound

  constructor(player) {
    for (let i = 0; i < player.children.length; i++) {
      if (player.children[i].classList.value.split(" ").includes("video")) this.video = player.children[i]
      if (player.children[i].classList.value.split(" ").includes("progress")) this.progress = player.children[i]
      if (player.children[i].classList.value.split(" ").includes("play")) this.play = player.children[i]
      if (player.children[i].classList.value.split(" ").includes("speed")) this.speed = player.children[i]
      if (player.children[i].classList.value.split(" ").includes("zoom")) this.zoom = player.children[i]
      if (player.children[i].classList.value.split(" ").includes("sound")) this.sound = player.children[i]
    }
  }

  event(e) {
    if (e["path"]["0"].classList.value.split(" ").includes("play") && !this.status) this.start()
    else if (e["path"]["0"].classList.value.split(" ").includes("play") && this.status) this.stop()
    if (e["path"]["0"].classList.value.split(" ").includes("speed")) this.#changeSpeed()
    if (e["path"]["0"].classList.value.split(" ").includes("sound")) this.#changeSound()
    if (e["path"]["0"].classList.value.split(" ").includes("progress")) this.#changeTime(e)
    if (e["path"]["0"].classList.value.split(" ").includes("zoom")) this.#changeZoom()
  }

  start() {
    this.video.play()
    this.status = true
    this.play.innerText = "| |"
  }

  stop() {
    this.video.pause()
    this.status = false
    this.play.innerText = "►"
  }

  changeProgress() {
    this.progress.value = this.video.currentTime / this.video.duration * 100
  }

  #changeSpeed() {
    this.video.playbackRate = parseFloat(this.speed.value.replace(",", "."))
  }

  #changeSound() {
    this.video.volume = this.sound.value / 100
  }

  #changeZoom() {
    if (!this.statusZoom) {
      document.documentElement.webkitRequestFullscreen()
      this.statusZoom = true
    } else if (this.statusZoom) {
      document.webkitCancelFullScreen()
      this.statusZoom = false
    }
  }

  #changeTime(e) {
    this.progress.value = 100 * this.progress.offsetWidth / e.offsetX
    this.video.currentTime = this.video.duration * (
      e.offsetX / this.progress.offsetWidth
    )
  }
}

function newVideoPlayer(videoPlayer) {
  let video = new Player(videoPlayer)
  videoPlayer.addEventListener("click", e => {video.event(e)})
  videoPlayer.addEventListener("change", e => {video.event(e)})
  videoPlayer.querySelector(".video").addEventListener("timeupdate", e => {video.changeProgress()})
}

newVideoPlayer(document.querySelector(".video_player"))
newVideoPlayer(document.querySelector(".video_player2"))





































// a.#changeSpeed()












//
