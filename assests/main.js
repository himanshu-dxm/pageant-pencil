console.log("Hello")

const copyBtns = [...document.getElementsByClassName('share')]

console.log(copyBtns)

copyBtns.forEach(btn => btn.addEventListener('click', () => {
    // console.log('Click')
    const link = btn.getAttribute('link')
        // console.log(link)
    navigator.clipboard.writeText(link)
}));

const like_btn = [...document.getElementsByClassName('heart')]

console.log(like_btn)

like_btn.forEach(btn => btn.addEventListener('click', () => {
    console.log('click')
    btn.style.color = "red"
        // document.getElementsByClassName('heart').style.color("red");
}));