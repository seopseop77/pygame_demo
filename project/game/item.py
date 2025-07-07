import pygame
from .game_object import GameObject
from config import TILE_SIZE, ITEM_SIZE, COLORS

class Item(GameObject):
    """Base collectible item.

    Default color is yellow for coins (255, 215, 0) or green (0, 255, 0)
    """

    def __init__(self, x, y, item_type, color=None):
        if color is None:
            if item_type == "coin":
                color = COLORS["coin"]
            else:
                color = COLORS["speed"]
        super().__init__(
            x + (TILE_SIZE - ITEM_SIZE) // 2,
            y + (TILE_SIZE - ITEM_SIZE) // 2,
            ITEM_SIZE,
            ITEM_SIZE,
            color=color,
        )
        self.item_type = item_type


class SpeedBoostItem(Item):
    """Permanently increases player's speed.

    Cyan square (0, 255, 255)
    """

    def __init__(self, x, y):
        super().__init__(x, y, "speed", color=COLORS["speed"])


class InvincibilityItem(Item):
    """Grants temporary invincibility.

    Yellow square (255, 255, 0)
    """

    def __init__(self, x, y):
        super().__init__(x, y, "invincibility", color=COLORS["invincibility"])


class ProjectileItem(Item):
    """Allows the player to shoot projectiles.

    Purple square (200, 0, 200)
    """

    def __init__(self, x, y):
        super().__init__(x, y, "projectile", color=COLORS["projectile_item"])
