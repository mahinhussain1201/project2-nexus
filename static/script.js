function filterPortfolio(button) {
    var typeToFilter = button.innerHTML;
    var portfolioItems = document.querySelectorAll('.card1');

    portfolioItems.forEach(function (item) {
        var itemType = item.getAttribute('data-type');
        var display = (typeToFilter === 'All' || typeToFilter === itemType) ? 'block' : 'none';
        item.style.display = display;
    });

    // Toggle 'off' class for all buttons
    document.querySelectorAll('.toggler_btn').forEach(function (btn) {
        btn.classList.toggle('off', btn !== button);
    });
}

function hideAlert() {
    var alertElement = document.getElementById('myAlert');
    if (alertElement) {
        alertElement.classList.add('hidden'); // Add a class to hide the alert
    }
}

// Set a timeout to call hideAlert after 2000 milliseconds (2 seconds)
setTimeout(hideAlert, 2000);