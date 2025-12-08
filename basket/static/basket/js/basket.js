document.addEventListener("DOMContentLoaded", function () {
    // Update item quantity
    $(".update-link").click(function (e) {
        e.preventDefault();
        const form = $(this)
            .closest(".basket-actions-wrapper")
            .find(".update-form");
        form.submit();
    });

    // Remove item with custom confirmation modal
    let removeUrl = null;
    let removeCsrf = null;
    let removeModal = null;

    const modalEl = document.getElementById("removeItemModal");
    if (modalEl) {
        removeModal = new bootstrap.Modal(modalEl);
    }

    $(".remove-item").click(function (e) {
        e.preventDefault();

        if (!removeModal) {
            if (confirm("Are you sure you want to remove this item from your basket?")) {
                const url = $(this).data("url");
                const csrf = $(this).data("csrf");
                $.post(url, { csrfmiddlewaretoken: csrf }).done(function () {
                    location.reload();
                });
            }
            return;
        }

        removeUrl = $(this).data("url");
        removeCsrf = $(this).data("csrf");

        const itemName = $(this).data("item-name") || "this item";
        $("#removeItemName").text(itemName);

        removeModal.show();
    });

    // Handle confirm button click and remove item from basket
    $("#confirmRemoveBtn").click(function () {
        if (!removeUrl || !removeCsrf) {
            return;
        }

        $.post(removeUrl, {
            csrfmiddlewaretoken: removeCsrf,
        }).done(function () {
            // Close modal + reload page to reflect changes
            removeModal.hide();
            location.reload();
        });
    });
});
