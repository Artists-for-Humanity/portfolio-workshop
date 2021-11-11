function slide_menu() {
    const slide_menu = document.querySelector('.slide_menu')
    if (slide_menu.dataset.open == "true") {
        console.log("closed")
        slide_menu.dataset.open = "false"
    } else {
        console.log("open")
        slide_menu.dataset.open = "true"
    }
}