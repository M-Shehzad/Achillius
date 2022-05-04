//gsap animations
// gsap.registerPlugin(ScrollTrigger);
// let tl = new gsap.timeline();

gsap.from('.stg1',{
    scrollTrigger:{
        trigger:'#about',
        // markers:true,
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
        // markers:true,
        start:'top center'
    },
    opacity:0,
    y:50,
    stagger:.3,
    duration:.5
})


gsap.from('.stg3',{
    scrollTrigger:{
        trigger:'#cars',
        // markers:true,
        start:'top center'
    },
    opacity:0,
    y:50,
    stagger:.3,
    duration:.5
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



