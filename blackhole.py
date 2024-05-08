import math
import grid 

class BlackHole():
    def __init__(self, x, y, prop) -> None:
        self.x = x
        self.y = y
        self.radius = math.floor(self.x * prop) // 2  # later gamer can change size, the space time bend changes, thus lensing affect is more intense
        self.curve = self.radius * 2

    def space_time_range(self, x, y):
        distance_squared = (x - self.x) ** 2 + (y - self.y) ** 2
        return distance_squared <= self.curve ** 2

    def event_horizon_range(self, x, y):
        distance_squared = (x - self.x) ** 2 + (y - self.y) ** 2
        return distance_squared <= self.radius ** 2
    
    def copied_object(self, x, y):
        return (-x, -y)
        

    
    
    
