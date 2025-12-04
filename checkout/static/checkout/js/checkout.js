let stripe;
let card;
let clientSecret;
let isProcessing = false;
let cardComplete = false;
let cardError = null;

// Validate form 
function isFormValid() {
    const fullName = document.getElementById("id_full_name");
    const email = document.getElementById("id_email");
    const phone = document.getElementById("id_phone_number");
    const address1 = document.getElementById("id_street_address1");
    const city = document.getElementById("id_town_or_city");
    const postcode = document.getElementById("id_postcode");
    const country = document.getElementById("id_country");

    const requiredFields = [fullName, email, phone, address1, city, postcode, country];

    return requiredFields.every(field => field && field.value.trim() !== "");
}

// Enable/disable the submit button based on validity + card status
function updateSubmitState() {
    const submitButton = document.getElementById("submit-btn");
    const shouldEnable = isFormValid() && cardComplete && !cardError && !isProcessing;
    submitButton.disabled = !shouldEnable;
}

// Sets up Stripe on page load, creates a PaymentIntent, and mounts the card element
document.addEventListener("DOMContentLoaded", async () => {
    stripe = Stripe(STRIPE_PUBLIC_KEY);

    const response = await fetch("/checkout/create-payment-intent/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({})
    });

    const data = await response.json();

    if (data.error) {
        showError(data.error);
        return;
    }

    clientSecret = data.clientSecret;
    const elements = stripe.elements();
    const style = {
        base: {
            color: "var(--color-3)",
            fontFamily: "var(--font-family-1)",
            fontSmoothing: "antialiased",
            fontSize: "16px",
            "::placeholder": {
                color: "var(--color-10)"
            },
            ":-webkit-autofill": {
                color: "var(--color-3)",
            },
        },
        invalid: {
            color: "#e5424d",
            iconColor: "#e5424d",
        },
    };

    card = elements.create("card", {
        style: style
    });
    card.mount("#card-element");

    card.on("change", function (event) {
        const displayError = document.getElementById("error-message");
        if (event.error) {
            displayError.textContent = event.error.message;
            cardError = event.error.message;
        } else {
            displayError.textContent = "";
            cardError = null;
        }

        cardComplete = event.complete === true;
        updateSubmitState();
    });

    const form = document.getElementById("payment-form");
    form.addEventListener("submit", handleSubmit);

    const submitButton = document.getElementById("submit-btn");
    submitButton.disabled = true;

    const watchedFields = [
        "id_full_name",
        "id_email",
        "id_phone_number",
        "id_street_address1",
        "id_town_or_city",
        "id_postcode",
        "id_country"
    ];

    watchedFields.forEach(id => {
        const el = document.getElementById(id);
        if (!el) return;
        const eventName = el.tagName === "SELECT" ? "change" : "input";
        el.addEventListener(eventName, updateSubmitState);
    });
});

// Handles form submission and payment confirmation
async function handleSubmit(e) {
    e.preventDefault();

    if (isProcessing) return;
    isProcessing = true;

    setLoading(true);

    const fullName = document.getElementById("id_full_name");
    const email = document.getElementById("id_email");
    const phone = document.getElementById("id_phone_number");
    const address1 = document.getElementById("id_street_address1");
    const address2 = document.getElementById("id_street_address2");
    const city = document.getElementById("id_town_or_city");
    const postcode = document.getElementById("id_postcode");
    const country = document.getElementById("id_country");

    const billingDetails = {
        name: fullName.value.trim(),
        email: email.value.trim(),
        phone: phone.value.trim(),
        address: {
            line1: address1.value.trim(),
            line2: address2.value.trim(),
            city: city.value.trim(),
            postal_code: postcode.value.trim(),
            country: country.value,
        },
    };

    const shippingDetails = {
        name: fullName.value.trim(),
        phone: phone.value.trim(),
        address: {
            line1: address1.value.trim(),
            line2: address2.value.trim(),
            city: city.value.trim(),
            postal_code: postcode.value.trim(),
            country: country.value,
        },
    };

    toggleFormDisabled(true);
    card.update({ disabled: true });

    console.log("Client secret:", clientSecret);

    let result;
    try {
        result = await stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: billingDetails,
            },
            shipping: shippingDetails,
        });
    } catch (err) {
        console.error("Stripe threw an error:", err);
        showError("There was a problem confirming your payment. Please try again.");
        resetProcessingState();
        return;
    }

    const { error, paymentIntent } = result;

    if (error) {
        console.error("Stripe error:", error);
        showError(error.message);
        resetProcessingState();
        return;
    }

    if (paymentIntent && paymentIntent.status === "succeeded") {
        console.log("Payment succeeded, submitting form to Django…");
        const form = document.getElementById("payment-form");
        HTMLFormElement.prototype.submit.call(form);
    } else {
        showError("Payment did not complete. Please try again.");
        resetProcessingState();
    }
}


// Display message in event of error
function showError(messageText) {
    const messageContainer = document.querySelector("#error-message");
    messageContainer.textContent = messageText;

    setTimeout(function () {
        messageContainer.textContent = "";
    }, 5000);
}

// Show loading state on the submit button
function setLoading(isLoading) {
    const submitButton = document.getElementById("submit-btn");
    const spinner = document.getElementById("button-spinner");
    const btnContent = submitButton.querySelector(".btn-content");

    if (isLoading) {
        submitButton.disabled = true;
        btnContent.style.opacity = "0";
        spinner.classList.remove("hidden");
    } else {
        submitButton.disabled = false;
        btnContent.style.opacity = "1";
        spinner.classList.add("hidden");
    }
}

// Disable form fields when submit button is clicked
function toggleFormDisabled(disabled) {
    const form = document.getElementById("payment-form");
    const elements = form.querySelectorAll("input, select, button, textarea");
    elements.forEach(element => {
        if (element.name === "csrfmiddlewaretoken") {
            return;
        }
        if (element.id !== "submit-btn") {
            element.disabled = disabled;
        }
    });
}

// Reset loading state and re-enable form
function resetProcessingState() {
    setLoading(false);
    toggleFormDisabled(false);
    card.update({ disabled: false });
    isProcessing = false;
}

// Full form validation
document.addEventListener("DOMContentLoaded", function () {
    const fields = document.querySelectorAll("input.form-control");

    fields.forEach(field => {
        if (field.id === "card-element") return;

        const error = document.createElement("div");
        error.classList.add("invalid-feedback");
        error.style.display = "none";
        error.textContent = "This field is required.";
        field.parentNode.appendChild(error);

        function validateField() {
            const value = field.value.trim();
            if (value === "") {
                field.classList.remove("is-invalid");
                error.style.display = "none";
                return;
            }

            let isValid = true;

            if (field.type === "email") {
                isValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
                if (!isValid) {
                    error.textContent = "Please enter a valid email address.";
                }
            }

            if (field.id === "id_phone_number") {
                const digits = value.replace(/\D/g, "");
                isValid = digits.length >= 7 && digits.length <= 15;
                if (!isValid) {
                    error.textContent = "Please enter a valid phone number.";
                }
            }
            if (!isValid) {
                field.classList.add("is-invalid");
                error.style.display = "block";
            } else {
                field.classList.remove("is-invalid");
                error.style.display = "none";
            }
        }

        ["input", "blur", "change"].forEach(evt =>
            field.addEventListener(evt, validateField)
        );
        validateField();
    });
});