import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

def load_data(file_path):
    # Load the extended dataset from a CSV file
    data = pd.read_csv(file_path)
    return data[['temperature', 'smoke_level', 'gas_level']]

def train_anomaly_model(data):
    # Train an Isolation Forest model
    model = IsolationForest(contamination=0.1)
    model.fit(data)
    return model

if __name__ == "__main__":
    # Load the dataset from sensor_data_extended.csv
    data = load_data("data/sample_data.csv")

    # Train the model
    model = train_anomaly_model(data)

    # Save the trained model to a file
    joblib.dump(model, "models/anomaly_model.pkl")
