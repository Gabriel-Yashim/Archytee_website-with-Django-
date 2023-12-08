// slider functionality for the home page hero section 
const reviewContainer = document.querySelector('.slider-wrapper');
const nxtBtn = document.querySelector('.nxt-btn');
const preBtn = document.querySelector('.prev-btn');

let containerDimensions = reviewContainer.getBoundingClientRect();
let containerWidth = containerDimensions.width;

nxtBtn.addEventListener('click', () => {
    reviewContainer.scrollLeft += containerWidth;
})

preBtn.addEventListener('click', () => {
    reviewContainer.scrollLeft -= containerWidth;
})

// toggle button functionality on tab and mobile view
const mainmenu = document.querySelector('.mainmenu');
const openmenu = document.querySelector('.openmenu');


openmenu.addEventListener('click', ()=> {
    mainmenu.classList.toggle('active')
});


function initializeSlider(sliderClassName) {
    var slideIndex = 1;
    showDivs(slideIndex, sliderClassName);

    function plusDivs(n) {
        showDivs(slideIndex += n, sliderClassName);
    }

    function showDivs(n, className) {
        var i;
        var x = document.getElementsByClassName(className);
        if (n > x.length) slideIndex = 1;
        if (n < 1) slideIndex = x.length;
        for (i = 0; i < x.length; i++) {
            x[i].style.display = "none";
        }
        x[slideIndex - 1].style.display = "block";
    }

    // Return plusDivs function
    return plusDivs;
}

// Initialize sliders and get the plusDivs functions
var plusDivs1 = initializeSlider("mySlides1");
var plusDivs2 = initializeSlider("mySlides2");
var plusDivs3 = initializeSlider("mySlides3");
var plusDivs4 = initializeSlider("mySlides4");

// Attach click event listeners to buttons
document.querySelector('.button1').addEventListener('click', function () {
    plusDivs1(1);
});

document.querySelector('.button2').addEventListener('click', function () {
    plusDivs2(1);
});

document.querySelector('.button3').addEventListener('click', function () {
    plusDivs3(1);
});

document.querySelector('.button4').addEventListener('click', function () {
    plusDivs4(1);
});

document.querySelector('.openmenu').addEventListener('click', function () {
    document.querySelector('.mainmenu').classList.toggle('active');
});
