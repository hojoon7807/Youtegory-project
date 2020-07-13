const currentLocation = location.href

const sideBar = document.querySelector('.sidebar')
const menu = sideBar.querySelectorAll('a')

for (let i = 0; i < menu.length; i++) {

    if (menu[i].href === currentLocation) {
        menu[i].className = "active"
    }
}
const homeBtn = document.querySelector('leftArea')
