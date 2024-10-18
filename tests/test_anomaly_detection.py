import unittest
from models.anomaly_detection import AnomalyDetector

class TestAnomalyDetection(unittest.TestCase):
    def test_detect_anomaly(self):
        detector = AnomalyDetector()
        test_data = {'temperature': 90, 'smoke_level': 0.9, 'gas_level': 0.8}
        result = detector.detect(test_data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
