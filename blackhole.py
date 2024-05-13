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
        angle_radians = math.atan2(y - self.y, x - self.x)
        change_x_angle = 0
        change_y_angle = 0
        copied_x = -(math.floor(x - self.x) * 2) + x
        copied_y = -(math.floor(y - self.y) * 2) + y
        
        match angle_radians:
            case angle_radians > 0 and angle_radians < math.pi / 2: # Q1
                diff = math.pi / 2 - angle_radians
                scale_factor = 1 / diff
                copied_x *= scale_factor 
            case angle_radians > math.pi / 2 and angle_radians < math.pi: # Q2
                pass
            case angle_radians < -math.pi / 2 and angle_radians > -math.pi: # Q3
                pass
            case angle_radians < 0 and angle_radians > -math.pi / 2: # Q4
                pass 
       
        return copied_x, copied_y
        

    
    
    
