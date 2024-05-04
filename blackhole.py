import math

class BlackHole:
    def __init__(self, x, y, prop) -> None:
        self.x = x
        self.y = y
        self.radius = math.floor(self.x * prop) // 2  # later gamer can change size, the space time bend changes, thus lensing affect is more intense
