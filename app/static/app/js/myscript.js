$('#slider1, #slider2, #slider3,#slider4', ).owlCarousel({
    loop: true,
    margin: 25,
    responsiveClass: true,
    autoplayTimeout: 3000,
    dots: true,
    autoplayHoverPause: true,
    responsive: {
        0: { items: 1, nav: false, autoplay: true },
        600: { items: 3, nav: true, autoplay: true },
        1000: { items: 4, nav: true, loop: true, autoplay: true }
    }
});