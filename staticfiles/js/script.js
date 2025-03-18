document.addEventListener('DOMContentLoaded', function () {
    const themeLink = document.getElementById('theme-link');
    const toggleButton = document.getElementById('toggle-theme-btn');

    // Check session storage for theme preference
    const currentTheme = "{{ request.session.darkmode }}";

    if (currentTheme === 'True') {
        themeLink.href = "{% static 'css/dark.css' %}";
        document.body.classList.add('dark-mode');
    } else {
        themeLink.href = "{% static 'css/light.css' %}";
        document.body.classList.remove('dark-mode');
    }

    // Toggle theme on button click
    toggleButton.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent default form submission
        const isDarkMode = document.body.classList.contains('dark-mode');

        if (isDarkMode) {
            themeLink.href = "{% static 'css/light.css' %}";
            document.body.classList.remove('dark-mode');
        } else {
            themeLink.href = "{% static 'css/dark.css' %}";
            document.body.classList.add('dark-mode');
        }

        // Save preference in session storage
        fetch("{% url 'toggle_theme' %}", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({ darkmode: !isDarkMode })
        });
    });
});
