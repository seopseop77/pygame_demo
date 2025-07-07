import pygame
from .game_object import GameObject

TILE_SIZE = 32

COLOR_MAP = {
    '#': (100, 100, 100),  # Solid wall/ground - gray
    '.': (0, 0, 0),        # Empty background - black
    'E': (0, 200, 0),      # Goal tile - green
}

class Tile(GameObject):
    """Environment tile used for collision."""

    def __init__(self, x, y, tile_type):
        color = COLOR_MAP.get(tile_type, (100, 100, 100))
        super().__init__(x, y, TILE_SIZE, TILE_SIZE, color=color)
        self.tile_type = tile_type


class GoalTile(Tile):
    """Special tile marking the level goal."""

    def __init__(self, x, y):
        super().__init__(x, y, 'E')
