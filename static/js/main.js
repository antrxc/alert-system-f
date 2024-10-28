function updateSensorData() {
    fetch('/api/sensor-data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('temperature').textContent = data.temperature.toFixed(1);
            document.getElementById('smokeLevel').textContent = data.smoke_level.toFixed(3);
            document.getElementById('gasLevel').textContent = data.gas_level.toFixed(3);
            document.getElementById('lastUpdated').textContent = `Last Updated: ${data.last_updated}`;

            const statusElement = document.getElementById('systemStatus');
            if (data.is_anomalous) {
                statusElement.textContent = 'System Status: ALERT!';
                statusElement.classList.add('alert');
            } else {
                statusElement.textContent = 'System Status: Normal';
                statusElement.classList.remove('alert');
            }
        })
        .catch(error => console.error('Error fetching sensor data:', error));
}

// Update data every 5 seconds
setInterval(updateSensorData, 5000);

// Initial update
updateSensorData();
