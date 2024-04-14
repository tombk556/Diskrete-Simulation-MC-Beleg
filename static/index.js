document.addEventListener('DOMContentLoaded', function() {
    let temperatureChart;  // Declare this outside to make it accessible in the update function
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

            // Check if the chart exists and destroy it
            if (temperatureChart) {
                temperatureChart.destroy();
            }

            // Create a new chart instance
            const ctx = document.getElementById('chart').getContext('2d');
            temperatureChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.days,
                    datasets: [
                    {
                        label: 'Mean Temperature',
                        data: data.mean_temperature,
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1,
                        yAxisID: 'y-temperature'
                    },
                    {
                        label: 'Mean Revenue',
                        data: data.mean_revenue,
                        backgroundColor: 'rgba(54, 162, 235, 0.2)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1,
                        yAxisID: 'y-finances'
                    },
                    {
                        label: 'Mean Profit',
                        data: data.mean_profit,
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1,
                        yAxisID: 'y-finances'
                    }]
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
                                drawOnChartArea: false // this ensures grid lines only for finances
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error:', error));
    });
});
