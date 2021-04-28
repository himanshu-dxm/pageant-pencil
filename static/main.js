console.log("Hello")

const copyBtns = [...document.getElementsByClassName('share')]

console.log(copyBtns)

copyBtns.forEach(btn => btn.addEventListener('click', () => {
    // console.log('Click')
    const link = btn.getAttribute('link')
        // console.log(link)
    navigator.clipboard.writeText(link)
}))