document.addEventListener("DOMContentLoaded", function() {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            var spinnerElement = document.getElementById('spinner');
            if (spinnerElement) {
                spinnerElement.classList.remove('show');
            }
        }, 1);
    };
    spinner();

    // Initiate wowjs
    // This would require you to include WOW.js in your project or convert its functionality to vanilla JS as well
    if (typeof WOW === "function") {
        new WOW().init();
    }

    // Sticky Navbar
    window.addEventListener('scroll', function () {
        var navBar = document.querySelector('.nav-bar');
        if (window.scrollY > 45) {
            navBar.classList.add('sticky-top');
        } else {
            navBar.classList.remove('sticky-top');
        }
    });

    // Back to top button
    var backToTopButton = document.querySelector('.back-to-top');
    window.addEventListener('scroll', function () {
        if (window.scrollY > 300) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });
    backToTopButton.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    setTimeout(function() {
        var message = document.getElementById('message');
        if (message) {
            var fadeEffect = setInterval(function () {
                if (!message.style.opacity) {
                    message.style.opacity = 1;
                }
                if (message.style.opacity > 0) {
                    message.style.opacity -= 0.1;
                } else {
                    clearInterval(fadeEffect);
                    message.style.display = 'none'; // Optionally hide the element completely after fading out
                }
            }, 200); // Adjust this value to control the speed of the fade out
        }
    }, 3000);
    
    

    // Header carousel and Testimonials carousel
    // Conversion for these would depend on the implementation of owlCarousel in vanilla JS
    // You'd need a vanilla JS carousel library or write your own implementation.
});
