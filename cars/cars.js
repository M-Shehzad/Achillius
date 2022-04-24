
//Pagination
var swiper = new Swiper(".mySwiper", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});

//animations
// gsap.from('.stg-E2',{
//     scrollTrigger:{
//         trigger:'#responsibility',
//         // markers:true,
//         start:'top center'
//     },
//     opacity:0,
//     y:50,
//     stagger:.3,
//     duration:.5
// })
gsap.to('.raptor1 .swiper-slide .content',{
    opacity:100,
    y:-50,
    duration:1.5,
    delay:0.5
})

gsap.from('.car-details  *',{
    scrollTrigger:{
        trigger:'.car-details',
        // markers:true,
        start:'top center'
    },
    opacity:0,
    y:50,
    stagger:.3,
    duration:.5
})

gsap.from('.news .stg',{
    scrollTrigger:{
        trigger:'.news',
        // markers:true,
        start:'top center'
    },
    opacity:0,
    y:50,
    stagger:.3,
    duration:.5
})
gsap.from('.gallery .stg',{
    scrollTrigger:{
        trigger:'.gallery',
        // markers:true,
        start:'top center'
    },
    opacity:0,
    y:50,
    stagger:.3,
    duration:.5
})

