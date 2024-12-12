function redirectToPage(page) {
    window.location.href = page;
  }


 // Script to show options when dropdown is clicked
 function toggleDropdown(dropdownId, containerId) {
    const container = document.getElementById(containerId);
    if (container.style.display === "none" || container.style.display === "") {
        container.style.display = "block";
    } else {
        container.style.display = "none";
    }
}

// Script to handle selected checkboxes display
function updateSelectedStores() {
    const checkboxes = document.querySelectorAll('input[name="stores"]:checked');
    const selectedText = Array.from(checkboxes).map(cb => cb.value).join(', ');
    document.getElementById('selected-stores').innerText = selectedText || "None selected";
}

// Before submitting the form, populate the hidden fields
function populateFormData() {
    const location = document.querySelector('input[name="location"]:checked');
    if (location) {
        document.getElementById('location-input').value = location.value;
    }

    const selectedStores = Array.from(document.querySelectorAll('input[name="stores"]:checked')).map(cb => cb.value);
    document.getElementById('stores-input').value = selectedStores.join(',');
}

// Attach the function to form submit event
document.querySelector('form').addEventListener('submit', populateFormData);
