import random

class SensorService:
    def __init__(self):
        self.temperature_range = (20, 30)
        self.smoke_range = (0, 0.2)
        self.gas_range = (0, 0.1)

    def get_data(self):
        temperature = self._simulate_reading(self.temperature_range)
        smoke_level = self._simulate_reading(self.smoke_range)
        gas_level = self._simulate_reading(self.gas_range)

        return {
            'temperature': temperature,
            'smoke_level': smoke_level,
            'gas_level': gas_level
        }

    def _simulate_reading(self, normal_range):
        if random.random() < 0.001:
            return self._simulate_anomaly(normal_range)

        return random.uniform(*normal_range)

    def _simulate_anomaly(self, normal_range):
        factor = random.uniform(1.5, 3)
        return normal_range[1] * factor
