const slides = document.querySelectorAll('.slide_image');
let index = 0;

function showSlide(i) {
    slides.forEach((slide, idx) => {
        slide.classList.toggle('active', idx === i);
    });
}

document.getElementById('nextbtn').addEventListener('click', () => {
    index = (index + 1) % slides.length;
    showSlide(index);
});

document.getElementById('prevbtn').addEventListener('click', () => {
    index = (index - 1 + slides.length) % slides.length;
    showSlide(index);
});

showSlide(index);
