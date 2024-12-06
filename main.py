import logging
from services.sensor_service import SensorService
from services.alert_service import AlertService
from models.anomaly_detection import AnomalyDetector
from flask import Flask, render_template, jsonify
import threading
import datetime
import time
import numpy as np
import os
import pytz

ist = pytz.timezone('Asia/Kolkata')
# Initialize Flask app
app = Flask(__name__)

# Global variable to store the latest sensor data
latest_data = {
    'temperature': 0,
    'smoke_level': 0,
    'gas_level': 0,
    'is_anomalous': False,
    'last_updated': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.route('/')
def index():
    """Serve the main dashboard."""
    return render_template('index.html')

@app.route('/api/sensor-data', methods=['GET'])
def get_sensor_data():
    """
    API endpoint to fetch the latest sensor data.
    """
    global latest_data

    # Debugging: Log the structure of latest_data
    import logging
    logging.info(f"Raw latest_data: {latest_data}")

    # Ensure all ndarrays are converted to lists before serialization
    sanitized_data = convert_ndarray_to_list(latest_data)

    # Return the sanitized data
    return jsonify(sanitized_data)



def convert_ndarray_to_list(data):
    """
    Recursively converts all NumPy ndarrays in a data structure to lists.
    Handles dictionaries, lists, and NumPy arrays.
    """
    if isinstance(data, dict):
        return {key: convert_ndarray_to_list(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_ndarray_to_list(element) for element in data]
    elif isinstance(data, np.ndarray):
        return data.tolist()
    return data


def run_monitoring():
    """
    Continuously monitor sensor data, detect anomalies, and send alerts if necessary.
    """
    global latest_data
    sensor_service = SensorService()
    alert_service = AlertService()
    anomaly_detector = AnomalyDetector()

    while True:
        # Fetch sensor data
        data = sensor_service.get_data()
        
        # Convert all NumPy arrays in `data` to lists
        data = convert_ndarray_to_list(data)

        is_anomalous = anomaly_detector.detect(data)

        # Update the global latest_data dictionary
        latest_data = {
            **data,
            'is_anomalous': is_anomalous,
            'last_updated': datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")
        }

        # Send alerts if an anomaly is detected
        if is_anomalous:
            logging.info("Anomaly detected! Sending alerts.")
            message = f"Alert: Anomaly detected in sensor data! Details: {data}"
            alert_service.send_sms('+919043395259', message)
            alert_service.make_call('+919043395259', message)

        # Sleep for 5 seconds before the next monitoring iteration
        time.sleep(5)


if __name__ == "__main__":
    # Start the monitoring thread
    monitoring_thread = threading.Thread(target=run_monitoring, daemon=True)
    monitoring_thread.start()

    # Run the Flask app
    app.run(debug=True, port=8080)
