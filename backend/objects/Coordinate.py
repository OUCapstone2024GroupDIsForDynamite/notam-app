class Coordinate:
    def __init__(self, latitude, longitude):
        self.x = latitude
        self.y = longitude

    def __repr__(self):
        return f"Coordinate(x={self.latitude}, y={self.longitude})"