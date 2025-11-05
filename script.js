document.getElementById('saveBtn').addEventListener('click', function() {
  const word = document.getElementById('word').value.trim();
  const meaning = document.getElementById('meaning').value.trim();
  const resultDiv = document.getElementById('result');

  if (word && meaning) {
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = `<strong>${word}:</strong> ${meaning}`;
    document.getElementById('word').value = '';
    document.getElementById('meaning').value = '';
  } else {
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = 'Please fill in both fields!';
  }
});
