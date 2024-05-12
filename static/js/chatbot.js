window.onload = function () {
    const form = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const voiceInput = document.getElementById('voice-input');
    const voiceButton = document.getElementById('voice-button');

    // Check if browser supports SpeechRecognition
    if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();

        voiceButton.onclick = function () {
            recognition.start();
        };

        recognition.onstart = function () {
            console.log('Voice recognition started');
        };

        recognition.onresult = function (event) {
            const transcript = event.results[0][0].transcript;
            voiceInput.value = transcript;
            userInput.value = transcript; // Optionally set the transcript as the text input value
        };

        recognition.onerror = function (event) {
            console.error('Speech recognition error:', event.error);
        };
    } else {
        console.error('Speech recognition not supported');
        voiceButton.disabled = true;
    }
};