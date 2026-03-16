document.addEventListener("DOMContentLoaded", function () {
    const announcementBar = document.getElementById("announcement-bar");
    const closeBar = document.getElementById("close-bar");

    setTimeout(function () {
        announcementBar.classList.add("show");
    }, 300);

    closeBar.addEventListener("click", function () {
        announcementBar.style.display = "none";
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const announcementBar = document.getElementById("announcement-bar");
    const closeBar = document.getElementById("close-bar");

    if (announcementBar && closeBar) {
        setTimeout(function () {
            announcementBar.classList.add("show");
        }, 300);

        closeBar.addEventListener("click", function () {
            announcementBar.style.display = "none";
        });
    }

    const eventHero = document.getElementById("event-hero");

    if (eventHero) {
        const heroImages = [
            "/static/heritage_event_centre_app/images/event6.jpg",
            "/static/heritage_event_centre_app/images/event4.jpg",
            "/static/heritage_event_centre_app/images/event3.jpg",
            "/static/heritage_event_centre_app/images/conference_Hall.jpg"
        ];

        let currentImageIndex = 0;

        function changeHeroBackground() {
            eventHero.style.backgroundImage = `url("${heroImages[currentImageIndex]}")`;
            currentImageIndex = (currentImageIndex + 1) % heroImages.length;
        }

        changeHeroBackground();
        setInterval(changeHeroBackground, 4000);
    }
});


document.addEventListener("DOMContentLoaded", function () {
    const closeBar = document.getElementById("close-bar");
    const announcementBar = document.getElementById("announcement-bar");

    if (closeBar && announcementBar) {
        closeBar.addEventListener("click", function () {
            announcementBar.style.display = "none";
        });
    }
});