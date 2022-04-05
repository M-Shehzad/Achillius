const navLinks = document.querySelector('header nav');
const header = document.querySelector('header');
document.addEventListener('DOMContentLoaded', (event) => {
    window.scrollTo(0, 0);
});

//navbar function
let prevScrollPos = window.scrollY;
window.addEventListener('scroll',()=>{
    let currentScrollPos = window.scrollY;
    //navbar background changer
    header.classList.toggle('sticky',currentScrollPos> 0);
    if(header.classList.contains('sticky')){
        navLinks.style.backgroundColor='#323232';
    }else{
        navLinks.style.backgroundColor='transparent';
    }

    if(currentScrollPos < prevScrollPos){
        document.querySelector('header').style.transform = 'translateY(0%)';
    }else{
        //only push the navbar out if the navbar isnt open
        if(!navLinks.classList.contains('active')){
            document.querySelector('header').style.transform = 'translateY(-100%)';
        }
    }
    prevScrollPos = currentScrollPos;
    // console.log(window.scrollY);
})

// responsive navbar
const toggleButton = document.getElementById('menu-bars');

toggleButton.addEventListener('click',()=>{
    navLinks.classList.toggle('active');
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