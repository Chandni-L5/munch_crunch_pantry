// Size card selection
document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".size-card.selectable");

    cards.forEach(card => {
        card.addEventListener("click", () => {
            cards.forEach(c => c.classList.remove("selected"));
            card.classList.add("selected");
        });
    });
});

// Dropdown chevron rotation on info sections
document.addEventListener("DOMContentLoaded", () => {
    const toggles = document.querySelectorAll(".dropdown-toggle-section");

    toggles.forEach(toggle => {
        const chevron = toggle.querySelector(".chevron-icon");
        const target = document.querySelector(toggle.getAttribute("href"));

        target.addEventListener("show.bs.collapse", () => {
            chevron.classList.add("chevron-rotate");
        });

        target.addEventListener("hide.bs.collapse", () => {
            chevron.classList.remove("chevron-rotate");
        });
    });
});
