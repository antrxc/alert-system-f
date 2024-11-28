import pandas as pd
import joblib
import warnings
from sklearn.ensemble import IsolationForest

# Filter out the specific UserWarning about feature names
warnings.filterwarnings('ignore', category=UserWarning, message='X does not have valid feature names*')

class AnomalyDetector:
    def __init__(self, model_path='models/anomaly_model.pkl'):
        self.model = joblib.load(model_path)

    def detect(self, data):
    # Ensure the data contains the required features
        expected_features = ['temperature', 'smoke_level', 'gas_level']
        if not all(feature in data for feature in expected_features):
            raise ValueError(f"Missing one or more required features: {expected_features}")
    
    # Validate that the features have the correct types (e.g., float for sensor readings)
        for feature in expected_features:
            if not isinstance(data[feature], (int, float)):
                raise TypeError(f"The feature '{feature}' must be a number (int or float).")
    
    # Format the data in the same order as the model expects
        values = [[data[feature] for feature in expected_features]]
    
    # Predict whether the data point is an anomaly (-1 for anomaly, 1 for normal)
        prediction = self.model.predict(values)[0]
    
        if prediction == -1:
            return True  # Anomaly detected
        else:
            return False  # Data is normal


    def _load_training_data(self, file_path='data/sample_data.csv'):
        data = pd.read_csv(file_path)
        return data[['temperature', 'smoke_level', 'gas_level']]

if __name__ == "__main__":
    detector = AnomalyDetector()

    # New sensor data for anomaly detection
    new_sensor_data = {
        'temperature': 35.0,
        'smoke_level': 0.1,
        'gas_level': 0.15
    }

    if detector.detect(new_sensor_data):
        print("Anomaly detected!")
    else:
        print("Data is normal.")
