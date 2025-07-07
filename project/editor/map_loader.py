"""Utility module for loading maps from text files."""
import os
from typing import List, Tuple

from game.tile import Tile, GoalTile
from game.player import Player
from game.enemy import Enemy
from game.item import Item, SpeedBoostItem, InvincibilityItem, ProjectileItem
from config import TILE_SIZE


def load_map(file_path: str) -> Tuple[List[List[str]], Player, list, list, list]:
    """Load a map from a text file and instantiate game objects."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        lines = [list(line.strip()) for line in f.readlines()]

    rows = len(lines)
    cols = len(lines[0]) if rows else 0

    tiles = []
    enemies = []
    items = []
    player = Player(0, 0)

    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            world_x = x * TILE_SIZE
            world_y = y * TILE_SIZE
            if char == '#':
                tiles.append(Tile(world_x, world_y, '#'))
            elif char == 'P':
                player.rect.topleft = (world_x, world_y)
            elif char == 'G':
                enemies.append(Enemy(world_x, world_y))
            elif char == 'C':
                items.append(Item(world_x, world_y, 'coin'))
            elif char == 'S':
                items.append(SpeedBoostItem(world_x, world_y))
            elif char == 'I':
                items.append(InvincibilityItem(world_x, world_y))
            elif char == 'F':
                items.append(ProjectileItem(world_x, world_y))
            elif char == 'E':
                tiles.append(GoalTile(world_x, world_y))
    player.spawn = player.rect.topleft
    return lines, player, tiles, enemies, items


def save_map(file_path: str, map_data: List[List[str]]):
    """Save the map data back to a text file."""
    with open(file_path, "w", encoding="utf-8") as f:
        for row in map_data:
            f.write("".join(row) + "\n")
