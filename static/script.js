document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.buttons button');
    const cards = document.querySelectorAll('.portfolio_container .card');

    buttons.forEach(button => {
        button.addEventListener('click', function () {
            // Remove 'active' class from all buttons
            buttons.forEach(b => b.classList.remove('active'));

            // Add 'active' class to the clicked button
            this.classList.add('active');

            // Show/hide cards based on the selected category
            const category = this.id;
            cards.forEach(card => {
                const cardCategory = card.dataset.category;
                card.style.display = (category === 'all' || category === cardCategory) ? 'block' : 'none';
            });
        });
    });
});