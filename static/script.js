async function predictMessage() {

    const message = document.getElementById("message").value;

    if (!message.trim()) {
        alert("Please enter a message.");
        return;
    }

    const response = await fetch("/predict", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })

    });

    const result = await response.json();

    const isSpam = result.spam === 1;

    const spamText = isSpam ? "SPAM" : "HAM";

    const sentimentText =
        result.sentiment.charAt(0).toUpperCase() +
        result.sentiment.slice(1);

    const confidence =
        (result.confidence * 100).toFixed(2);

    const resultClass = isSpam ? "spam-result" : "ham-result";

    document.getElementById("result").innerHTML = `

        <h2>Prediction Result</h2>

        <div class="${resultClass}">
            ${spamText}
        </div>

        <p>
            <strong>Sentiment:</strong>
            ${sentimentText}
        </p>

        <p>
            <strong>Confidence:</strong>
            ${confidence}%
        </p>

        <div class="confidence-bar">
            <div
                class="confidence-fill"
                style="width: ${confidence}%"
            ></div>
        </div>

    `;
}