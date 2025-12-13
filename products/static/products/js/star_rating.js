document.addEventListener("DOMContentLoaded", function () {
        document.querySelectorAll("form").forEach(form => {
            const ratingField = form.querySelector("#id_rating");
            const stars = form.querySelectorAll(".star-rating .star");

            if (!ratingField || !stars.length) return;

            let currentRating = parseInt(ratingField.value || "0", 10);

            function paint(rating) {
                stars.forEach(star => {
                    const v = parseInt(star.dataset.value, 10);
                    star.classList.toggle("active", v <= rating);
                    star.textContent = v <= rating ? "★" : "☆";
                });
            }

            paint(currentRating);

            stars.forEach(star => {
                const value = parseInt(star.dataset.value, 10);

                star.addEventListener("mouseenter", () => paint(value));
                star.addEventListener("mouseleave", () => paint(currentRating));

                star.addEventListener("click", () => {
                    currentRating = value;
                    ratingField.value = value;
                    paint(value);
                });
            });
        });
    });