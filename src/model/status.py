from datetime import datetime

class Status():
    def __init__(self, timestamp, location, batterylevel):
        self.location = location
        self.batterylevel = batterylevel
        self.date = datetime.fromtimestamp(timestamp)

