document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('chart').getContext('2d');
    let temperatureChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [
                {
                    label: 'Temperatur (°C)',
                    data: [],
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1,
                    yAxisID: 'y-temperature'
                },
                {
                    label: 'Umsatz (€)',
                    data: [],
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1,
                    yAxisID: 'y-finances'
                },
                {
                    label: 'Gewinn (€)',
                    data: [],
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    yAxisID: 'y-finances'
                }
            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    position: 'left',
                    id: 'y-temperature'
                },
                yFinances: {
                    beginAtZero: true,
                    position: 'right',
                    id: 'y-finances',
                    grid: {
                        drawOnChartArea: false
                    }
                }
            }
        }
    });

    const button = document.querySelector('.button');
    button.addEventListener('click', function(e) {
        e.preventDefault();

        const anzahl = document.getElementById('anzahlInput').value;
        const fixkosten = document.getElementById('fixkostenInput').value;
        const variableKosten = document.getElementById('variableKostenInput').value;
        const temperatur = document.getElementById('temperaturInput').value;

        fetch('/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ anzahl, fixkosten, variableKosten, temperatur })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('outputProfit').value = data.total_profit;
            document.getElementById('outputUmsatz').value = data.total_revenue;
            document.getElementById('outputGaeste').value = data.total_customers;

            temperatureChart.data.labels = data.days;
            temperatureChart.data.datasets[0].data = data.mean_temperature;
            temperatureChart.data.datasets[1].data = data.mean_revenue;
            temperatureChart.data.datasets[2].data = data.mean_profit;
            temperatureChart.update();
        })
        .catch(error => console.error('Error:', error));
    });
});
