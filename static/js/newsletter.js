document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("newsletter-form");
    const emailInput = document.getElementById("newsletter-email");
    const responseBox = document.getElementById("newsletter-response");
    const banner = document.getElementById("newsletter-banner");

    if (!banner || !form || !emailInput) return;

    const STORAGE_KEY = "newsletterSubscribed";

    // If already subscribed, hide the banner
    if (localStorage.getItem(STORAGE_KEY) === "true") {
        banner.style.display = "none";
        return;
    }

    // Handle form submission
    form.addEventListener("submit", function (e) {
        e.preventDefault(); 
        const email = emailInput.value.trim();

        if (!email) {
            showMessage("Please enter a valid email address.", "danger");
            return;
        }

        // Success message
        showMessage("🎉 Thank you for subscribing!", "success");

        // Store subscription status in localStorage
        localStorage.setItem("newsletterSubscribed", "true");

        // Hide the banner after subscription
        setTimeout(() => {
            banner.classList.add("fade-out");
            setTimeout(() => {
                banner.style.display = "none";
            }, 600);
        }, 2000);
    });

    function showMessage(message, type) {
        responseBox.style.display = "block";
        responseBox.className = "";
        responseBox.classList.add("alert", `alert-${type}`);
        responseBox.textContent = message;
    }
});
