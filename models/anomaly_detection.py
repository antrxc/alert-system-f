import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

class AnomalyDetector:
    def __init__(self, model_path='models/anomaly_model.pkl'):
        self.model = joblib.load(model_path)

    def detect(self, data):
        values = [[data['temperature'], data['smoke_level'], data['gas_level']]]
        return self.model.predict(values) == -1

    def _load_training_data(self, file_path='data/sample_data.csv'):
        data = pd.read_csv(file_path)
        return data[['temperature', 'smoke_level', 'gas_level']]


if __name__ == "__main__":
    detector = AnomalyDetector()

    new_sensor_data = {
        'temperature': 35.0,
        'smoke_level': 0.06,
        'gas_level': 0.02
    }

    if detector.detect(new_sensor_data):
        print("Anomaly detected!")
    else:
        print("Data is normal.")
