// script.js

document.addEventListener("DOMContentLoaded", function() {
    const gallery = document.querySelector(".gallery");
    const images = [
        "image1.jpg",
        "image2.jpg",
        "image3.jpg",
        "image4.jpg",
        "image5.jpg",
        "image6.jpg"
    ];

    // Function to create image elements and add them to the gallery
    function createGalleryImages() {
        images.forEach(function(imageSrc) {
            const img = document.createElement("img");
            img.src = imageSrc;
            img.alt = "Gallery Image";
            img.classList.add("gallery-image");
            gallery.appendChild(img);

            // Add a click event listener to each image to open a larger view
            img.addEventListener("click", function() {
                openImage(imageSrc);
            });
        });
    }

    // Function to open a larger view of the clicked image
    function openImage(imageSrc) {
        const overlay = document.createElement("div");
        overlay.classList.add("overlay");

        const largerImage = document.createElement("img");
        largerImage.src = imageSrc;
        largerImage.alt = "Larger Image";

        overlay.appendChild(largerImage);

        overlay.addEventListener("click", function() {
            overlay.remove();
        });

        document.body.appendChild(overlay);
    }

    // Call the function to create the gallery images
    createGalleryImages();
});
