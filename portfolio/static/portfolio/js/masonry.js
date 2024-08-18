document.addEventListener("DOMContentLoaded", function() {
    const images = document.querySelectorAll(".masonry-grid img");

    images.forEach(img => {
        img.addEventListener("load", () => {
            img.classList.add("loaded");
        });
    });
});