//gsap animations
gsap.registerPlugin(ScrollTrigger);
// let tl = new gsap.timeline();

gsap.from('.stg1',{
    scrollTrigger:{
        trigger:'#about',
        markers:true,
        start:'top center'
    },
    opacity:0,
    y:50,
    stagger:.3,
    // ease:Power4.easeOut,
    duration:.5
})


gsap.from('.stg2',{
    scrollTrigger:{
        trigger:'#department',
        markers:true,
        start:'top center'
    },
    opacity:0,
    y:50,
    stagger:.3,
    duration:.5
})
gsap.from('.stg3',{
    scrollTrigger:{
        trigger:'#contact',
        markers:true,
        start:'top center'
    },
    opacity:0,
    y:50,
    stagger:.3,
    duration:.5
})

// gsap.from('.box',{
//     scrollTrigger:{
//         trigger:'.box',
//         markers:true,
//         start:'top center'
//     },
//     opacity:0,
//     y:50,
//     stagger:.2,
//     duration:.5
// })


const navLinks = document.querySelector('header nav');
const header = document.querySelector('header');
// document.addEventListener('DOMContentLoaded', (event) => {
//     window.scrollTo(0, 0);
// });

//navbar function
let prevScrollPos = window.scrollY;
window.addEventListener('scroll',()=>{
    let currentScrollPos = window.scrollY;
    //navbar background changer
    header.classList.toggle('colorChanger',currentScrollPos> 0);
    // if(navLinks.classList.contains('active') || header.classList.contains('colorChanger')){
    //     navLinks.style.backgroundColor='#000';
    // }else{
    //     navLinks.style.backgroundColor='transparent';
    // }

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
    header.classList.add('colorChanger');
    navLinks.classList.toggle('active');
})


//underline function
// let section = document.querySelectorAll('section');
// window.onscroll = ()=>{
//     section.forEach(sec=>{
//         let top = window.scrollY;
//         let height = sec.offsetHeight;
//         let offset = sec.offsetTop-200;
//         let id = sec.getAttribute('id');
//         if(top >= offset && top<offset+height){
//             document.querySelector("#"+id+' .underline').style.transform="scaleX(1)";
//         }
//     })
// }

//current year
document.querySelector('#currentYear').innerText = new Date().getFullYear();

