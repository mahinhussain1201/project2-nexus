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

