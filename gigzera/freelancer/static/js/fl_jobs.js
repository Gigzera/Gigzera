// JavaScript for video slideshow
let currentVideoIndex = 0;
const videoContainers = document.querySelectorAll(".ad-video-container");
const videos = document.querySelectorAll("video");

// Function to show the next video after the current one ends
function showNextVideo() {
  // Hide current video
  videoContainers[currentVideoIndex].classList.remove("active");

  // Move to the next video
  currentVideoIndex = (currentVideoIndex + 1) % videoContainers.length;

  // Show the next video
  videoContainers[currentVideoIndex].classList.add("active");

  // Ensure that the video starts playing when switched
  videos[currentVideoIndex].play();
}

// Attach the 'ended' event listener to each video
videos.forEach((video, index) => {
  video.addEventListener("ended", () => {
    // Show next video when the current video ends
    showNextVideo();
  });
});

// Ensure the videos are loaded and ready to play
window.addEventListener("load", () => {
  // Preload videos
  videos.forEach((video) => {
    video.load();
  });
});

// Start the slideshow when the page is loaded
window.onload = function () {
  const videos = document.querySelectorAll("video");

  // Start the first video only if a video exists
  if (videos.length > 0) {
    videos[0].play();
  }

  // Start the image slideshow
  startImageSlideshow();
};

// Function to start the image slideshow for ad-boxes
// function startImageSlideshow() {
//   const adBoxes = document.querySelectorAll(".ad-box .ad-slideshow");

//   adBoxes.forEach((adBox) => {
//     // Skip the video box (first box)
//     if (adBox.querySelector(".ad-video-container")) return;

//     const images = adBox.querySelectorAll(".ad-image-container");
//     let activeIndex = 0;

//     // Set the first image to active initially
//     images[activeIndex].classList.add("active");

//     // Change the active image every 3 seconds (5000 milliseconds)
//     setInterval(() => {
//       images[activeIndex].classList.remove("active"); // Hide the current image
//       activeIndex = (activeIndex + 1) % images.length; // Move to the next image (circular)
//       images[activeIndex].classList.add("active"); // Show the next image
//     }, 5000); // 3 seconds interval
//   });
// }

// New
// function startImageSlideshow() {
//   const adBoxes = document.querySelectorAll(".ad-box .ad-slideshow");

//   adBoxes.forEach((adBox) => {
//     const images = adBox.querySelectorAll(".ad-image-container");

//     if (images.length === 0) return; // If no images, skip

//     let activeIndex = 0;
//     images[activeIndex].classList.add("active");

//     setInterval(() => {
//       images[activeIndex].classList.remove("active"); // Hide current image
//       activeIndex = (activeIndex + 1) % images.length; // Move to next image
//       images[activeIndex].classList.add("active"); // Show next image

//       // ** Dynamically update the href based on the active image **
//       const activeImageContainer = images[activeIndex];
//       const linkElement = activeImageContainer.querySelector("a");

//       if (linkElement) {
//         // ✅ Ensure the <a> tag exists before using .href
//         const newLink = linkElement.href;

//         // Find the currently active <a> tag and update its href
//         const adLink = adBox.querySelector(".ad-link");
//         if (adLink) {
//           adLink.href = newLink;
//         }
//       }
//     }, 5000); // Change every 5 seconds
//   });
// }

function startImageSlideshow() {
  const adBoxes = document.querySelectorAll(".ad-box .ad-slideshow");

  adBoxes.forEach((adBox) => {
    const images = adBox.querySelectorAll(".ad-image-container");

    if (images.length === 0) return; // Skip if no images

    let activeIndex = 0;
    images[activeIndex].classList.add("active");

    setInterval(() => {
      images[activeIndex].classList.remove("active"); // Hide current image
      activeIndex = (activeIndex + 1) % images.length; // Move to next image
      images[activeIndex].classList.add("active"); // Show next image
    }, 5000); // Change every 5 seconds
  });
}

// //Pop up javascript
function openModal(opportunityId, curSymbol, duration, budget) {
  // Set values in the modal fields
  document.getElementById("quote_opportunityId").value = opportunityId;
  document.getElementById("quote_currency").innerText = curSymbol;
  document.getElementById("budget").placeholder = budget;
  document.getElementById("timeline").placeholder = duration;

  // Show the modal
  document.getElementById("quoteModal").classList.remove("hidden");
}

function closeModal() {
  document.getElementById("quoteModal").classList.add("hidden");
}
// Javascript for modal open for provide quote
// function openModal(opportunityId) {
//   console.log(opportunityId, "ID is coming");
//   document.getElementById("quote_opportunityId").value = opportunityId;
//   // document.getElementById("quote_title").value = title;
//   // document.getElementById("quote_currency").value = curr;
//   // document.getElementById("quote_cur_symbol").value = cur_symbol;
//   document.getElementById("quoteModal").classList.remove("hidden");
// }

// // Close the modal
// function closeModal() {
//   document.getElementById("quoteModal").classList.add("hidden");
// }

// Close the modal when clicking outside the modal content
document.getElementById("quoteModal").addEventListener("click", function (e) {
  if (e.target === document.getElementById("quoteModal")) {
    closeModal();
  }
});

// Javascript for open modal at side bar for view more button
// Function to open the modal
function tailwindOpenModal() {
  // Show the overlay and popup
  document.getElementById("tailwind-overlay").classList.remove("hidden");
  document.getElementById("tailwind-popup").classList.remove("hidden");
}

// Function to close the modal
function tailwindCloseModal() {
  // Hide the overlay and popup
  document.getElementById("tailwind-overlay").classList.add("hidden");
  document.getElementById("tailwind-popup").classList.add("hidden");
}

// Event listener for the close button inside the popup
document
  .getElementById("tailwind-close-drawer")
  .addEventListener("click", tailwindCloseModal);

// Event listener for clicking outside the popup to close the modal
document
  .getElementById("tailwind-overlay")
  .addEventListener("click", tailwindCloseModal);

// Jobs slider on the left
// Slideshow functionality
const slidesLeft = document.querySelectorAll(".slide-left");
let currentSlideLeft = 0; // Start at the first slide

// Function to show the current slide
function showSlideLeft(index) {
  slidesLeft.forEach((slide, i) => {
    slide.classList.remove("active");
    if (i === index) {
      slide.classList.add("active");
    }
  });
}

// Initialize the slideshow
showSlideLeft(currentSlideLeft);

// Automatic slide transition every 5 seconds
setInterval(() => {
  currentSlideLeft = (currentSlideLeft + 1) % slidesLeft.length;
  showSlideLeft(currentSlideLeft);
}, 5000);

const filterInput = document.getElementById("job-filter");
const jobCards = document.querySelectorAll(".job-card");
filterInput.addEventListener("input", function () {
  const filterValue = filterInput.value.toLowerCase();

  jobCards.forEach((card) => {
    const jobTitle = card.getAttribute("data-title").toLowerCase();

    if (jobTitle.includes(filterValue)) {
      card.style.display = "block"; // Show the job card
    } else {
      card.style.display = "none"; // Hide the job card
    }
  });
});
