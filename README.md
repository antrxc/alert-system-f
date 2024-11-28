# Disaster Alert System

This is a production-level disaster alert system that uses anomaly detection from sensor data to alert emergency services, building owners, and nearby people. The system can be simulated with sensors for testing purposes and aims to detect disasters such as fire, gas leaks, and other emergencies.

## Features
- Sensor data simulation (temperature, gas, smoke)
- Anomaly detection using machine learning
- Alerts via SMS, calls, and notifications
- Emergency service triggers

## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd alert-system-f
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the System
1. Start the monitoring system:
    ```bash
    python main.py
    ```

2. The system will start a Flask web server and a background thread for monitoring sensor data.

### Testing
1. Run the unit tests:
    ```bash
    python -m unittest discover tests
    ```

## Code Overview

### Main Components
- `main.py`: Initializes and runs the Flask web server and the monitoring thread.
- `services/sensor_service.py`: Simulates sensor data.
- `services/alert_service.py`: Sends alerts via SMS and calls.
- `models/anomaly_detection.py`: Detects anomalies in sensor data using a pre-trained machine learning model.

### Key Classes and Methods
- `AnomalyDetector`: Loads a pre-trained Isolation Forest model to detect anomalies.
    - `detect(data)`: Returns `True` if the data is anomalous, otherwise `False`.
- `AlertService`: Sends alerts.
    - `send_sms(phone_number, message)`: Sends an SMS alert.
    - `make_call(phone_number, message)`: Makes a call with the alert message.
- `SensorService`: Simulates sensor data.
    - `get_data()`: Returns simulated sensor data.

### Example
To simulate sensor data and detect anomalies:
```python
from services.sensor_service import SensorService
from models.anomaly_detection import AnomalyDetector

sensor_service = SensorService()
anomaly_detector = AnomalyDetector()

data = sensor_service.get_data()
is_anomalous = anomaly_detector.detect(data)

if is_anomalous:
    print("Anomaly detected!")
else:
    print("Data is normal.")