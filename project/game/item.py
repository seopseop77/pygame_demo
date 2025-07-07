import pygame
from .game_object import GameObject

TILE_SIZE = 32

class Item(GameObject):
    """Collectible item."""

    def __init__(self, x, y, item_type):
        color = (255, 215, 0) if item_type == 'coin' else (0, 255, 0)
        super().__init__(x, y, TILE_SIZE, TILE_SIZE, color=color)
        self.item_type = item_type
