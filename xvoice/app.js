// Run Markov Algorithms
document.getElementById('runML').addEventListener('click', () => {
    const mlResults = document.getElementById('mlResults');
    mlResults.innerText = "Running Markov algorithms...";

    // Simulate running Markov algorithms
    setTimeout(() => {
        mlResults.innerText = "Optimal Policy: [0, 1, 0]\nState Values: [10, -1, -1]";
    }, 1000); // Simulate a delay for processing
});

// Color Picker
document.getElementById('color').addEventListener('input', (event) => {
    document.body.style.backgroundColor = event.target.value; // Change background color dynamically
});
