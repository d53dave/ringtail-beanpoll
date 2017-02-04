from datetime import datetime

class Temperature():
    def __init__(self, timestamp, temperature_val, location):
        self.timestamp = datetime.fromtimestamp(timestamp)
        self.temperature_val = temperature_val
        self.location = location
