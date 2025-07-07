import pygame
from .game_object import GameObject

TILE_SIZE = 32

class Projectile(GameObject):
    """Simple horizontal projectile.

    Dark gray rectangle (50, 50, 50)
    """

    def __init__(self, x, y, direction):
        super().__init__(x, y, 10, 4, color=(50, 50, 50))
        self.direction = direction
        self.speed = 8

    def update(self):
        self.rect.x += self.speed * self.direction

