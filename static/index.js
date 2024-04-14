document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector('.button'); // Make sure the button selector is correct
    button.addEventListener('click', function(e) {
        e.preventDefault();

        // Collect input data
        const anzahl = document.getElementById('anzahlInput').value;
        const fixkosten = document.getElementById('fixkostenInput').value;
        const variableKosten = document.getElementById('variableKostenInput').value;
        const temperatur = document.getElementById('temperaturInput').value;

        // Make POST request to the server
        fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ anzahl, fixkosten, variableKosten, temperatur })
        })
        .then(response => response.json())
        .then(data => {
            // Display total_profit in the output field
            document.getElementById('outputProfit').value = data.total_profit;
            document.getElementById('outputUmsatz').value = data.total_revenue;
        })
        .catch(error => console.error('Error:', error));
    });
});
