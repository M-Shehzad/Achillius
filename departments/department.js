// -------------Animations for department---------------
gsap.to('.stg-E1',{
    opacity:100,
    y:-50,
    delay:0.5,
    stagger:.5,
    duration:.5
})
gsap.from('.stg-E2',{
    scrollTrigger:{
        trigger:'#responsibility',
        // markers:true,
        start:'top center'
    },
    opacity:0,
    y:50,
    stagger:.3,
    duration:.5
})