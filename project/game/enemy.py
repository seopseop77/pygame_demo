import pygame
from .game_object import GameObject

TILE_SIZE = 32
MOVE_SPEED = 2

class Enemy(GameObject):
    """Simple enemy that walks left and right."""

    def __init__(self, x, y):
        super().__init__(x, y, TILE_SIZE, TILE_SIZE, color=(255, 0, 0))
        self.vel_x = MOVE_SPEED
        self.vel_y = 0

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
