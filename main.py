import logging
from services.sensor_service import SensorService
from services.alert_service import AlertService
from models.anomaly_detection import AnomalyDetector
from flask import Flask, render_template, jsonify
import threading
import datetime
import time
import os

app = Flask(__name__)

# Global variables to store latest data
latest_data = {
    'temperature': 0,
    'smoke_level': 0,
    'gas_level': 0,
    'is_anomalous': False,
    'last_updated': None
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/sensor-data')
def get_sensor_data():
    return jsonify(latest_data)

def run_monitoring():
    global latest_data
    sensor_service = SensorService()
    alert_service = AlertService()
    anomaly_detector = AnomalyDetector()

    while True:
        data = sensor_service.get_data()
        is_anomalous = anomaly_detector.detect(data)
        
        latest_data = {
            **data,
            'is_anomalous': is_anomalous,
            'last_updated': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        if is_anomalous:
            logging.info("Anomaly detected! Sending alerts.")
            message = f"Alert: Anomaly detected in sensor data! Details: {data}"
            alert_service.send_sms('+919043395259', message)
            alert_service.make_call('+919043395259', message)
            os._exit(0)

        time.sleep(5)  # Update every 5 seconds

if __name__ == "__main__":
    monitoring_thread = threading.Thread(target=run_monitoring)
    monitoring_thread.daemon = True
    monitoring_thread.start()
    
    app.run(debug=True)
