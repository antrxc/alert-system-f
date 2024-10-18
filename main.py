import logging
from services.sensor_service import SensorService
from services.alert_service import AlertService
from models.anomaly_detection import AnomalyDetector

def main():
    logging.basicConfig(level=logging.INFO)

    sensor_service = SensorService()
    alert_service = AlertService()
    anomaly_detector = AnomalyDetector()

    while True:
        data = sensor_service.get_data()

        is_anomalous = anomaly_detector.detect(data)

        if is_anomalous:
            logging.info("Anomaly detected! Sending alerts.")
            message = f"Alert: Anomaly detected in sensor data! Details: {data}"

            alert_service.send_sms('+919043395259', message)

        else:
            logging.info("All systems normal.")

if __name__ == "__main__":
    main()
