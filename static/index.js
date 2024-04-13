document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector('.button'); // Ensuring to select your button correctly, add an ID if necessary.
    button.addEventListener('click', function(e) {
        e.preventDefault();
        const anzahl = document.getElementById('anzahlInput').value;
        const fixkosten = document.getElementById('fixkostenInput').value;
        const variableKosten = document.getElementById('variableKostenInput').value;
        const temperatur = document.getElementById('temperaturInput').value;

        fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ anzahl, fixkosten, variableKosten, temperatur })
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
    });
});
