import pygame
from pygame import Vector2

class Blocks:

    def __init__(self, surface, color, position, size, rect):
        self.surface = surface
        self.color = color
        self.position = Vector2(position)
        self.size = Vector2(size)
        self.rect = pygame.Rect(self.position, self.size)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)
        widthdiff = 10
        height = 50
        bottomleft = Vector2((self.position.x), (self.position.y))
        topleft = Vector2((self.position.x + widthdiff), (self.position.y - height))
        bottomright = Vector2((self.position.x + self.size.x), (self.position.y))
        topright = Vector2((self.position.x + self.size.x - widthdiff), (self.position.y - height))
        trapezium_coords = [topleft, bottomleft, bottomright, topright]
        pygame.draw.polygon(self.surface, (125,125,125), trapezium_coords)


    def collision(self, circle_center, circle_radius):
        closest_x = max(self.position.x, min(circle_center.x, self.position.x + self.size.x))
        closest_y = max(self.position.y, min(circle_center.y, self.position.y + self.size.y))
        
        distance_vect = Vector2(closest_x - circle_center.x, closest_y - circle_center.y)
        
        if distance_vect.length() <= circle_radius*1.3:

            #When on top of the blocks
            if circle_center.y + circle_radius < closest_y:
                circle_center.y = closest_y - circle_radius - 1
                return "Bango_y"
            
            elif circle_center.y > closest_y:
                circle_center.y = closest_y + circle_radius + 1
                return "Bongo_y"
            
            #Both below are x axis collision detection
            if circle_center.x > self.position.x - 2:
                #circle_center.x = closest_x - circle_radius - 1
                return "Bango_x"
            
            if circle_center.x < self.position.x + self.size.x - 2:
                #circle_center.x += circle_radius
                return "Bongo_x"
            
        return False
    