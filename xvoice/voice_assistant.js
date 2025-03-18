let recognition = new webkitSpeechRecognition() || new SpeechRecognition();
recognition.lang = 'en-US';
recognition.maxResults = 10;

document.getElementById('start-button').addEventListener('click', () => {
    recognition.start();
    document.getElementById('start-button').disabled = true;
    document.getElementById('stop-button').disabled = false;
});

document.getElementById('stop-button').addEventListener('click', () => {
    recognition.stop();
    document.getElementById('start-button').disabled = false;
    document.getElementById('stop-button').disabled = true;
});

recognition.onresult = function(event) {
    let transcript = event.results[0][0].transcript;
    document.getElementById('output').innerText = transcript;

    // Send the transcript to Django for processing
    fetch('/process_voice/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query: 'What is the capital of France?' }),
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
