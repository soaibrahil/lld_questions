
class TemperatureSensor:
    def __init__(self):
        self._readings: list[float] = []

    def add_reading(self, value: float) -> None:
        # Only add if value is between -50 and 150 (inclusive)
        if value < -50 or value > 150:
            return False
        self._readings.append(value)
        return True

    def get_average(self) -> float:
        # Return the average of all readings, or 0.0 if no readings exist
        return round(sum(self._readings)/len(self._readings), 2) if len(self._readings) > 0 else 0.0

    def get_reading_count(self) -> int:
        # Return how many readings have been recorded
        return len(self._readings)

    def get_readings(self) -> list[float]:
        # Return a copy of the readings list (not the original)
        copy_reading = []
        for reading in self._readings:
            copy_reading.append(reading)
        return copy_reading


if __name__ == "__main__":
    sensor = TemperatureSensor()
    sensor.add_reading(22.5)
    sensor.add_reading(23.1)
    sensor.add_reading(200.0)  # Should be rejected
    sensor.add_reading(-10.0)

    print(f"Count: {sensor.get_reading_count()}")  # 3
    print(f"Average: {sensor.get_average()}")       # 11.87