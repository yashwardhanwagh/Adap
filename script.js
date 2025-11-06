const backendUrl = "http://127.0.0.1:5000"; // Flask backend URL

document.getElementById('saveBtn').addEventListener('click', async function() {
  const word = document.getElementById('word').value.trim();
  const meaning = document.getElementById('meaning').value.trim();
  const resultDiv = document.getElementById('result');

  if (!word || !meaning) {
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = '⚠️ Please fill in both fields!';
    return;
  }

  try {
    const response = await fetch(`${backendUrl}/add`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ word, meaning }),
    });

    const result = await response.json();

    if (response.ok) {
      resultDiv.style.display = 'block';
      resultDiv.innerHTML = `✅ <strong>${word}</strong> added successfully!`;
      document.getElementById('word').value = '';
      document.getElementById('meaning').value = '';
    } else {
      resultDiv.style.display = 'block';
      resultDiv.innerHTML = `❌ ${result.error || 'Something went wrong.'}`;
    }

  } catch (error) {
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = '🚫 Unable to connect to server. Is your backend running?';
    console.error(error);
  }
});
