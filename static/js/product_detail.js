document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".size-card.selectable");

    cards.forEach(card => {
        card.addEventListener("click", () => {
            // remove previous selection
            cards.forEach(c => c.classList.remove("selected"));

            // apply to clicked card
            card.classList.add("selected");
        });
    });
});