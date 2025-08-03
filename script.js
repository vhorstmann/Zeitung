document.getElementById('dataForm').addEventListener('submit', async function(e) {
  e.preventDefault();

  const birthdate = document.getElementById('birthdate').value;
  const years = document.getElementById('years').value;

  const responseDiv = document.getElementById('response');
  responseDiv.innerHTML = "Verarbeite Daten...";

  try {
    const res = await fetch('https://zeitung.onrender.com', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ birthdate, years })
    });

    const data = await res.json();
    responseDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
  } catch (error) {
    responseDiv.innerHTML = "Fehler beim Senden der Daten.";
    console.error(error);
  }
});
