document.addEventListener("DOMContentLoaded", function () {
    const banner = document.getElementById("newsletter-banner");
    const body = document.getElementById("newsletter-body");
    const toggleBtn = document.getElementById("newsletter-toggle");
    const toggleIcon = document.getElementById("newsletter-toggle-icon");

    const form = document.getElementById("newsletter-form");
    const emailInput = document.getElementById("newsletter-email");
    const responseBox = document.getElementById("newsletter-response");
    const submitBtn = document.getElementById("subscribe-btn");

    if (!banner || !body || !toggleBtn || !form || !emailInput || !responseBox) return;

    // minimise / expand
    toggleBtn.addEventListener("click", () => {
        const isHidden = body.style.display === "none";
        body.style.display = isHidden ? "block" : "none";
        toggleBtn.setAttribute("aria-expanded", isHidden);
        toggleBtn.querySelector("i").style.transform = isHidden ?
            "rotate(0deg)" :
            "rotate(-180deg)";
    });


    // CSRF helper
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(";").shift();
        return null;
    }

    // messages 
    function showMessage(message, type) {
        responseBox.style.display = "block";
        responseBox.className = "";
        responseBox.classList.add("alert", `alert-${type}`);
        responseBox.textContent = message;
    }

    // submit to backend
    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const email = emailInput.value.trim();
        if (!email) {
            showMessage("Please enter a valid email address.", "danger");
            return;
        }

        const postUrl = form.dataset.url;
        submitBtn.disabled = true;

        try {
            const res = await fetch(postUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                body: JSON.stringify({
                    email
                }),
            });

            const data = await res.json();

            if (!res.ok) {
                showMessage(
                    data.error || "Something went wrong. Please try again.",
                    "danger"
                );
                submitBtn.disabled = false;
                return;
            }

            showMessage(
                data.message || "🎉 Thank you for subscribing!",
                "success"
            );
            emailInput.value = "";
            submitBtn.disabled = false;

        } catch (err) {
            showMessage("Network error — please try again.", "danger");
            submitBtn.disabled = false;
        }
    });
});