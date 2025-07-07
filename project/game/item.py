import pygame
from .game_object import GameObject

TILE_SIZE = 32

class Item(GameObject):
    """Base collectible item.

    Default color is yellow for coins (255, 215, 0) or green (0, 255, 0)
    """

    def __init__(self, x, y, item_type, color=None):
        if color is None:
            color = (255, 215, 0) if item_type == "coin" else (0, 255, 0)
        super().__init__(x, y, TILE_SIZE, TILE_SIZE, color=color)
        self.item_type = item_type


class SpeedBoostItem(Item):
    """Permanently increases player's speed.

    Cyan square (0, 255, 255)
    """

    def __init__(self, x, y):
        super().__init__(x, y, "speed", color=(0, 255, 255))


class InvincibilityItem(Item):
    """Grants temporary invincibility.

    Yellow square (255, 255, 0)
    """

    def __init__(self, x, y):
        super().__init__(x, y, "invincibility", color=(255, 255, 0))


class ProjectileItem(Item):
    """Allows the player to shoot projectiles.

    Purple square (200, 0, 200)
    """

    def __init__(self, x, y):
        super().__init__(x, y, "projectile", color=(200, 0, 200))
