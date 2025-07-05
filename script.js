document.getElementById("explainBtn").addEventListener("click", async () => {
    const code = document.getElementById("codeInput").value;
    const output = document.getElementById("output");
    output.innerText = "⏳ Generating explanation...";

    try {
        const response = await fetch("http://127.0.0.1:5000/explain", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: code })
        });

        const data = await response.json();
        output.innerText = data.explanation;
    } catch (error) {
        output.innerText = "⚠️ Error generating explanation. Please make sure your backend is running.";
    }
});
