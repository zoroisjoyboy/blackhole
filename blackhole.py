import math
import grid 
import pygame

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
        
        distance = math.sqrt((x - self.x)**2 + (y - self.y)**2)

        copied_x = -(math.floor(x - self.x) * 2) + x
        copied_y = -(math.floor(y - self.y) * 2) + y

        angle = math.atan2(y - self.y, x - self.x)

        if x >= 0 and y >= 0:  # Q1
            pivot_angle = 0
        elif x < 0 and y >= 0:  # Q2
            pivot_angle = math.pi
        elif x < 0 and y < 0:  # Q3
            pivot_angle = math.pi
        else:  # Q4
            pivot_angle = 0

        angle_delta = (distance / self.radius) * math.pi 
        if angle < pivot_angle:
            angle += angle_delta
        elif angle > pivot_angle:
            angle -= angle_delta

        copied_x += self.radius * math.cos(angle) 
        copied_y += self.radius * math.sin(angle) 
        
        return copied_x, copied_y


  
    
    
