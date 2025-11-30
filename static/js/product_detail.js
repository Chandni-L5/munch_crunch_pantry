// Size card selection
document.addEventListener('DOMContentLoaded', function () {
    const sizeCards = document.querySelectorAll('.size-card.selectable');
    const pqInput = document.getElementById('product-quantity-id');
    const addBtn = document.querySelector('.add-to-basket-btn');

    if (addBtn) {
        addBtn.disabled = true;
        addBtn.classList.add('disabled-btn');
    }

    sizeCards.forEach(card => {
        card.addEventListener('click', function () {
            sizeCards.forEach(c => c.classList.remove('selected'));
            this.classList.add('selected');

            const pqId = this.dataset.pq
            if (pqInput) {
                pqInput.value = pqId;
            }

            if (addBtn) {
                addBtn.disabled = false;
                addBtn.classList.remove('disabled-btn');
            }
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
