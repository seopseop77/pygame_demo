import pygame
from .game_object import GameObject
from config import COLORS

class Projectile(GameObject):
    """Simple horizontal projectile.

    Dark gray rectangle (50, 50, 50)
    """

    def __init__(self, x, y, direction):
        super().__init__(x, y, 10, 4, color=COLORS["projectile"])
        self.direction = direction
        self.speed = 8

    def update(self):
        self.rect.x += self.speed * self.direction

