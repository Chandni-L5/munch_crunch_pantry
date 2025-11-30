document.addEventListener('DOMContentLoaded', function () {
    const sizeCards = document.querySelectorAll('.package-size-card.selectable');
    const pqInput = document.getElementById('product-quantity-id');
    const addBtn = document.querySelector('.add-to-basket-btn');
    const btnWrapper = document.querySelector('.btn-wrapper');

    if (!addBtn || !btnWrapper) return;

    // add to basket button disabled + tooltip visible + dimmed style
    addBtn.disabled = true;
    addBtn.classList.add('disabled-btn');
    btnWrapper.setAttribute('data-tooltip', 'Select a package size first');

    // Enable button + remove disabled style + remove tooltip
    sizeCards.forEach(card => {
        card.addEventListener('click', function () {
            sizeCards.forEach(c => c.classList.remove('selected'));
            this.classList.add('selected');

            const pqId = this.dataset.pq;
            if (pqInput) {
                pqInput.value = pqId;
            }

            addBtn.disabled = false;
            addBtn.classList.remove('disabled-btn');
            btnWrapper.removeAttribute('data-tooltip');
        });
    });
});


// Dropdown chevron rotation on info sections
document.addEventListener("DOMContentLoaded", () => {
    const toggles = document.querySelectorAll(".dropdown-toggle-section");

    toggles.forEach(toggle => {
        const chevron = toggle.querySelector(".chevron-icon");
        const target = document.querySelector(toggle.getAttribute("href"));

        if (!target) return;

        target.addEventListener("show.bs.collapse", () => {
            chevron.classList.add("chevron-rotate");
        });

        target.addEventListener("hide.bs.collapse", () => {
            chevron.classList.remove("chevron-rotate");
        });
    });
});
