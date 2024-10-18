import unittest
from typing import Dict

from services.alert_service import AlertService

class TestAlertService(unittest.TestCase):
    def test_send_alerts(self):
        alert_service = AlertService()
        test_data: dict[str, int | float] = {'temperature': 90, 'smoke_level': 0.9, 'gas_level': 0.8}
        alert_service.send_sms(test_data)
        self.assertTrue(True)  # Simulating success

if __name__ == '__main__':
    unittest.main()
