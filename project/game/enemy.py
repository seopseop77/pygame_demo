import pygame
from .game_object import GameObject
from config import TILE_SIZE, COLORS

MOVE_SPEED = -2

class Enemy(GameObject):
    """Simple enemy that walks left and right.

    Red square (255, 0, 0)
    """

    def __init__(self, x, y, point_value=100):
        super().__init__(x, y, TILE_SIZE, TILE_SIZE, color=COLORS["enemy"])
        self.vel_x = MOVE_SPEED
        self.vel_y = 0
        self.point_value = point_value

    def apply_gravity(self):
        self.vel_y += 0.5

    def update(self, tiles):
        """Move enemy and handle collisions."""
        self.apply_gravity()
        self.rect.x += self.vel_x
        for tile in tiles:
            if tile.tile_type == '#':
                if self.rect.colliderect(tile.rect):
                    if self.vel_x > 0:
                        self.rect.right = tile.rect.left
                        self.vel_x = -MOVE_SPEED
                    else:
                        self.rect.left = tile.rect.right
                        self.vel_x = MOVE_SPEED
        self.rect.y += self.vel_y
        for tile in tiles:
            if tile.tile_type == '#':
                if self.rect.colliderect(tile.rect):
                    if self.vel_y > 0:
                        self.rect.bottom = tile.rect.top
                        self.vel_y = 0
                    elif self.vel_y < 0:
                        self.rect.top = tile.rect.bottom
                        self.vel_y = 0
