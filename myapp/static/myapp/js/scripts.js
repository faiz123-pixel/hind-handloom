document.addEventListener('DOMContentLoaded', function () {
  const slides = document.querySelectorAll('.slide_image');
  const prevButton = document.getElementById('prevbtn');
  const nextButton = document.getElementById('nextbtn');
  let currentIndex = 0;
  const slideInterval = 3000;
  
  function nextSlide() {
      currentIndex = (currentIndex + 1) % slides.length; // Loop back to the first slide
      showSlide(currentIndex);
    }
    // Set the automatic slide interval
    const autoSlide = setInterval(nextSlide, slideInterval);
  // Show the initial slide
  showSlide(currentIndex);
  // Function to show a slide by index
  function showSlide(index) {
    slides.forEach((slide, i) => {
      slide.classList.remove('active');
      if (i === index) {
        slide.classList.add('active');
      }
    });
  }

  // Event listener for "Next" button
  nextButton.addEventListener('click', function () {
    currentIndex = (currentIndex + 1) % slides.length; // Loop back to the first slide
    showSlide(currentIndex);
  });

  // Event listener for "Previous" button
  prevButton.addEventListener('click', function () {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length; // Loop back to the last slide
    showSlide(currentIndex);
  });
});

function gotoproductdetail(productid) 
{
  window.location.href = `/product/${productid}/`;
}
