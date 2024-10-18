import csv
import random
import time

def simulate_sensor_data(file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['temperature', 'smoke_level', 'gas_level'])

        for _ in range(10000):
            temperature = random.uniform(20, 30)
            smoke_level = random.uniform(0, 0.2)
            gas_level = random.uniform(0, 0.1)

            if random.random() < 0.1:
                temperature = random.uniform(80, 120)
                smoke_level = random.uniform(0.5, 1.0)
                gas_level = random.uniform(0.3, 0.8)

            writer.writerow([temperature, smoke_level, gas_level])
            time.sleep(0.1)

if __name__ == "__main__":
    simulate_sensor_data('data/sample_data.csv')
