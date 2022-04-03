document.addEventListener('DOMContentLoaded', (event) => {
    window.scrollTo(0, 0);
});

//navbar function
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
    // console.log(window.scrollY);
})


//underline function
let section = document.querySelectorAll('section');
window.onscroll = ()=>{
    section.forEach(sec=>{
        let top = window.scrollY;
        let height = sec.offsetHeight;
        let offset = sec.offsetTop-150;
        let id = sec.getAttribute('id');
        if(top >= offset && top<offset+height){
            document.querySelector("#"+id+' .underline').style.transform="scaleX(1)";
        }
    })
}

//current year
document.querySelector('#currentYear').innerText = new Date().getFullYear();