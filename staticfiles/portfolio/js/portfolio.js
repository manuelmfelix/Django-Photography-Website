document.addEventListener('DOMContentLoaded', function() {
    const scrollContainer = document.querySelector('.scroll-gallery');
    const displayContainer = document.querySelector('.display-container');
    const displayImage = document.querySelector('.display-image');
    const closeButton = document.querySelector('.close-button');
    const header = document.querySelector('header');
    let lastScrollTop = 0;

    // Scroll horizontally with mouse wheel while pressing Shift
    scrollContainer.addEventListener('wheel', (evt) => {
        if (evt.shiftKey) {
            evt.preventDefault();
            scrollContainer.scrollLeft += evt.deltaY;
        }
    });

    // Always show the scrollbar
    scrollContainer.style.overflowX = 'auto';
    scrollContainer.style.overflowY = 'hidden'; // Ensure vertical scrollbar does not appear

    // Add click event listener to each image
    scrollContainer.querySelectorAll('.scroll-item').forEach(item => {
        item.style.cursor = 'pointer';
        item.addEventListener('click', () => {
            const img = item.querySelector('img');
            if (img) {
                displayImage.src = img.src;
                displayImage.style.maxWidth = '100%';
                displayImage.style.maxHeight = '100%';
                displayImage.style.objectFit = 'contain';
                displayContainer.style.display = 'flex';
            }
        });
    });

    // Add click event listener to close button
    closeButton.addEventListener('click', () => {
        displayContainer.style.display = 'none';
    });

    // Add click event listener to display container to close it when clicking outside the image
    displayContainer.addEventListener('click', (evt) => {
        if (evt.target !== displayImage) {
            displayContainer.style.display = 'none';
        }
    });

    // Function to check scroll position and toggle opacity
    function toggleHeaderVisibility() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        if (scrollTop > lastScrollTop) {
            // Scroll down
            header.style.transition = 'opacity 0.3s ease';
            header.style.opacity = '0';
        } else {
            // Scroll up or at the top
            header.style.transition = 'opacity 0.3s ease';
            header.style.opacity = '1';
        }

        lastScrollTop = scrollTop; // Update last scroll position
    }

    // Initially check scroll position
    toggleHeaderVisibility();

    // Listen to scroll events
    window.addEventListener('scroll', toggleHeaderVisibility);

});

