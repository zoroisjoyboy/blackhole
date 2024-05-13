import math
import grid 

class BlackHole():
    def __init__(self, x, y, prop) -> None:
        self.x = x
        self.y = y
        self.radius = math.floor(self.x * prop) // 2  # later gamer can change size, the space time bend changes, lensing affect is more intense
        self.curve = self.radius * 2

    def space_time_range(self, x, y):
        distance_squared = (x - self.x) ** 2 + (y - self.y) ** 2
        return distance_squared <= self.curve ** 2

    def event_horizon_range(self, x, y):
        distance_squared = (x - self.x) ** 2 + (y - self.y) ** 2
        return distance_squared <= self.radius ** 2
    
    def copied_object(self, x, y):
        angle_radians = math.atan2(y - self.y, x - self.x) # 2 sets of pivot points, if moving left/right then pi/2 if up and down 0/pi
        print(angle_radians)
        diff = math.pi / 2 - angle_radians
        change_x_angle = 0
        change_y_angle = 0
        scale_x = 0.3
        scale_y = 0.1
        copied_x = -(math.floor(x - self.x) * 2) + x
        copied_y = -(math.floor(y - self.y) * 2) + y
        
        if angle_radians > 0 and angle_radians < math.pi / 2: # Q1
            copied_x += -scale_x * math.cos(diff)
            copied_y += scale_y * math.sin(diff)
        elif angle_radians > math.pi / 2 and angle_radians < math.pi: # Q2
            copied_x += scale_x * math.cos(diff)
            copied_y += scale_y * math.sin(diff)
        elif angle_radians < -math.pi / 2 and angle_radians > -math.pi: # Q3
            copied_x += scale_x * math.cos(diff)
            copied_y += -scale_y * math.sin(diff)
        elif angle_radians < 0 and angle_radians > -math.pi / 2: # Q4
            copied_x += -scale_x * math.cos(diff)
            copied_y += -scale_y * math.sin(diff)

        print(copied_x, copied_y)
        return copied_x, copied_y
        

    
    
    
