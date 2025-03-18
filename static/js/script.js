document.addEventListener('DOMContentLoaded', function () {
    const colorPicker = document.getElementById('colorPicker');
    const applyColorBtn = document.getElementById('applyColorBtn');
    const exampleText = document.getElementById('exampleText');

    if (colorPicker && applyColorBtn && exampleText) {
        applyColorBtn.addEventListener('click', function () {
            const selectedColor = colorPicker.value;
            exampleText.style.color = selectedColor;

            // Save color in localStorage
            localStorage.setItem('selectedColor', selectedColor);
        });

        // Load saved color on page load
        const savedColor = localStorage.getItem('selectedColor');
        if (savedColor) {
            exampleText.style.color = savedColor;
            colorPicker.value = savedColor;
        }
    }
});
