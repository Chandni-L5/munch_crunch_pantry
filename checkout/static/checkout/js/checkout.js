let stripe;
let card;
let clientSecret;

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

    card = elements.create("card", { style: style });
    card.mount("#card-element");

    card.on("change", function (event) {
        const displayError = document.getElementById("error-message");
        if (event.error) {
            displayError.textContent = event.error.message;
        } else {
            displayError.textContent = "";
        }
    });
    const form = document.getElementById("payment-form");
    form.addEventListener("submit", handleSubmit);
});

// Handles form submission and payment confirmation
async function handleSubmit(e) {
    e.preventDefault();
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
    const { error, paymentIntent } = await stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: billingDetails,
        },
        shipping: shippingDetails,
    });

    if (error) {
        showError(error.message);
        setLoading(false);
    } else if (paymentIntent && paymentIntent.status === "succeeded") {
        window.location.href = "/checkout/success/";
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
    const submitButton = document.getElementById("submit");
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