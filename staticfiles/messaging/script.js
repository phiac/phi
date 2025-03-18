document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('theme-toggle');
    toggleButton.addEventListener('click', () => {
        document.body.dataset.theme =
            document.body.dataset.theme === 'dark' ? '' : 'dark';
    });
});
