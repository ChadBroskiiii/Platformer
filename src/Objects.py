import pygame
from pygame import Vector2


class Blocks:
    def __init__(self, surface, color, position, size, rect):
        self.surface = surface
        self.color = color
        self.position = Vector2(position)
        self.size = Vector2(size)
        self.rect = pygame.Rect(self.position, self.size)
        self.collisionrect = pygame.rect.Rect(self.position.x + 5, self.position.y - 17, self.size.x - 10, 26)

    def draw(self, offset=Vector2(0, 0)):
        # Draw the main rectangle
        relative_height = min(600-(self.position.y + self.size.y - offset.y), 0)
        pygame.draw.rect(self.surface, self.color, (
            self.position.x + offset.x,
            self.position.y + offset.y,
            self.size.x,
            self.size.y
        ))

        # Draw the trapezium
        width_diff = 10
        height = (50 - relative_height)* 0.2
        bottom_left = Vector2((self.position.x + offset.x), (self.position.y + offset.y))
        top_left = Vector2((self.position.x + width_diff + offset.x), (self.position.y + relative_height + height + offset.y))
        bottom_right = Vector2((self.position.x + self.size.x + offset.x), (self.position.y + offset.y))
        top_right = Vector2((self.position.x + self.size.x - width_diff + offset.x), (self.position.y + relative_height + height + offset.y))
        trapezium_coords = [top_left, bottom_left, bottom_right, top_right]
        pygame.draw.polygon(self.surface, (125, 125, 125), trapezium_coords)

    def collision(self, coordsx, coordsy, radius, platform):
        hitbox = pygame.rect.Rect(coordsx - radius, coordsy - radius, radius * 2, radius * 2)
        center = Vector2(coordsx + radius, coordsy + radius)

        topresult = pygame.Rect.colliderect(hitbox, self.collisionrect)
        result = pygame.Rect.colliderect(hitbox, platform)

        if result == True:
            return "other_coll"

        if topresult == True:
            return "top_coll"

        return False

    def get_position_y(self):
        return self.position.y - 17
    
    def get_main_position_y(self):
        return self.position.y
    
    def get_position_x(self):
        return self.position.x
    
    def get_size_y(self):
        return self.size.y
    
    def get_size_x(self):
        return self.size.x
