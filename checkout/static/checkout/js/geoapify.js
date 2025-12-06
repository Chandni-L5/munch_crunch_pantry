/* Core logic flow for this comes from here:
https://www.geoapify.com/tutorial/address-input-for-address-validation-and-address-verification-forms-tutorial/
*/

function addressAutocomplete(containerElement, callback, options) {
  // Find the existing input inside the container (crispy address_search field)
  const inputElement = containerElement.querySelector("input");

  if (!inputElement) {
    console.error("addressAutocomplete: No input element found inside container");
    return;
  }

  // The crispy structure is usually: <div> <label> <input> </div>
  // We'll attach dropdown + clear button to the input's parent
  const inputContainerElement = inputElement.parentElement;

  const MIN_ADDRESS_LENGTH = 3;
  const DEBOUNCE_DELAY = 300;

  let currentTimeout;
  let currentPromiseReject;
  let currentItems = [];
  let focusedItemIndex = -1;

  // --- Clear button ("X") ---
  const clearButton = document.createElement("div");
  clearButton.classList.add("clear-button");
  addIcon(clearButton);
  inputContainerElement.appendChild(clearButton);

  // Ensure we have a placeholder
  if (!inputElement.getAttribute("placeholder")) {
    inputElement.setAttribute(
      "placeholder",
      options && options.placeholder
        ? options.placeholder
        : "Start typing your address…"
    );
  }
  inputElement.setAttribute("autocomplete", "off");

  // --- Input handler ---
  inputElement.addEventListener("input", function () {
    const currentValue = this.value;

    // Toggle clear button visibility
    if (!currentValue) {
      clearButton.classList.remove("visible");
    } else {
      clearButton.classList.add("visible");
    }

    // Cancel previous debounce
    if (currentTimeout) {
      clearTimeout(currentTimeout);
    }

    // Cancel previous pending API call
    if (currentPromiseReject) {
      currentPromiseReject({ canceled: true });
      currentPromiseReject = null;
    }

    // Skip empty or too-short values
    if (!currentValue || currentValue.length < MIN_ADDRESS_LENGTH) {
      closeDropDownList();
      return;
    }

    // Debounce API call
    currentTimeout = setTimeout(() => {
      currentTimeout = null;

      const promise = new Promise((resolve, reject) => {
        currentPromiseReject = reject;

        // Use the global Django-injected key if available
        const apiKey =
          typeof GEOAPIFY_API_KEY !== "undefined"
            ? GEOAPIFY_API_KEY
            : "YOUR_API_KEY";

        // You can add filter=countrycode:gb if you want only UK:
        // &filter=countrycode:gb
        const url = `https://api.geoapify.com/v1/geocode/autocomplete?text=${encodeURIComponent(
          currentValue
        )}&format=json&limit=5&apiKey=${apiKey}`;

        fetch(url).then((response) => {
          currentPromiseReject = null;

          if (response.ok) {
            response.json().then((data) => resolve(data));
          } else {
            response.json().then((data) => reject(data));
          }
        });
      });

      promise.then(
        (data) => {
          currentItems = data.results || [];

          // Close old dropdown
          closeDropDownList();

          // Create dropdown container
          const autocompleteItemsElement = document.createElement("div");
          autocompleteItemsElement.setAttribute("class", "autocomplete-items");
          inputContainerElement.appendChild(autocompleteItemsElement);

          // Create an item for each result
          currentItems.forEach((result, index) => {
            const itemElement = document.createElement("div");
            itemElement.innerHTML = result.formatted;
            autocompleteItemsElement.appendChild(itemElement);

            itemElement.addEventListener("click", function () {
              inputElement.value = currentItems[index].formatted;
              callback(currentItems[index]);
              closeDropDownList();
            });
          });

          focusedItemIndex = -1;
        },
        (err) => {
          if (!err.canceled) {
            console.error(err);
          }
        }
      );
    }, DEBOUNCE_DELAY);
  });

  // --- Keyboard navigation ---
  inputElement.addEventListener("keydown", function (e) {
    const autocompleteItemsElement =
      inputContainerElement.querySelector(".autocomplete-items");

    if (autocompleteItemsElement) {
      const itemElements = autocompleteItemsElement.getElementsByTagName("div");
      if (!itemElements.length) return;

      if (e.key === "ArrowDown") {
        e.preventDefault();
        focusedItemIndex =
          focusedItemIndex !== itemElements.length - 1 ? focusedItemIndex + 1 : 0;
        setActive(itemElements, focusedItemIndex);
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        focusedItemIndex =
          focusedItemIndex > 0 ? focusedItemIndex - 1 : itemElements.length - 1;
        setActive(itemElements, focusedItemIndex);
      } else if (e.key === "Enter") {
        e.preventDefault();
        if (focusedItemIndex > -1) {
          itemElements[focusedItemIndex].click();
        }
      }
    } else {
      if (e.key === "ArrowDown") {
        const event = new Event("input", { bubbles: true });
        inputElement.dispatchEvent(event);
      }
    }
  });

  // --- Clear button behaviour ---
  clearButton.addEventListener("click", (e) => {
    e.stopPropagation();
    inputElement.value = "";
    clearButton.classList.remove("visible");
    closeDropDownList();
    callback(null);
  });

  // --- Close on outside click ---
  document.addEventListener("click", function (e) {
    if (!containerElement.contains(e.target)) {
      closeDropDownList();
    } else if (
      e.target === inputElement &&
      !inputContainerElement.querySelector(".autocomplete-items")
    ) {
      const event = new Event("input", { bubbles: true });
      inputElement.dispatchEvent(event);
    }
  });

  // --- Helpers ---
  function setActive(items, index) {
    if (!items || !items.length) return;

    for (let i = 0; i < items.length; i++) {
      items[i].classList.remove("autocomplete-active");
    }

    items[index].classList.add("autocomplete-active");

    if (currentItems[index]) {
      inputElement.value = currentItems[index].formatted;
      callback(currentItems[index]);
    }
  }

  function closeDropDownList() {
    const autocompleteItemsElement =
      inputContainerElement.querySelector(".autocomplete-items");
    if (autocompleteItemsElement) {
      inputContainerElement.removeChild(autocompleteItemsElement);
    }
    focusedItemIndex = -1;
  }

  function addIcon(buttonElement) {
    const svgElement = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svgElement.setAttribute("viewBox", "0 0 24 24");
    svgElement.setAttribute("height", "24");

    const iconElement = document.createElementNS("http://www.w3.org/2000/svg", "path");
    iconElement.setAttribute(
      "d",
      "M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"
    );
    iconElement.setAttribute("fill", "currentColor");

    svgElement.appendChild(iconElement);
    buttonElement.appendChild(svgElement);
  }
}
