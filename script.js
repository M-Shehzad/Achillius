


document.addEventListener('DOMContentLoaded', (event) => {
    window.scrollTo(0, 0);
});

let prevScrollPos = window.scrollY;
window.addEventListener('scroll',()=>{
    //navbar background changer
    document.querySelector('header').classList.toggle('sticky',window.scrollY > 0);

    let currentScrollPos = window.scrollY;
    if(currentScrollPos < prevScrollPos){
        document.querySelector('header').style.transform = 'translateY(0%)';
    }else{
        document.querySelector('header').style.transform = 'translateY(-100%)';
    }
    prevScrollPos = currentScrollPos;
    console.log(window.scrollY);
})
