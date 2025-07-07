# Pygame Platformer Demo

This repository contains a simple Mario-style side scrolling platformer built with Pygame.
All game objects are rendered using basic colored rectangles so no image assets
are required.

## Object Colors

- Player: blue
- Enemy: red
- Walls: gray
- Coins: yellow
- Speed boost: cyan
- Invincibility: yellow
- Projectile upgrade: purple
- Goal: green

## Running

```
python3 project/main.py [map_name]
```
If no map name is supplied, `level1.txt` is used. Sample maps are located in
`project/maps/` and demonstrate the various items and goal tiles.

Press `E` during the game to open the map editor. Use `1`-`5` to change tiles, left click to place, right click to erase, `S` to save, and `ESC` to return to the game.

## Controls

- **Left/Right Arrow**: Move
- **Up Arrow**: Jump
- **Space**: Shoot (after collecting projectile item)
- **E**: Open map editor
- **Esc**: Exit editor
- **S**: Save map in editor
- **1-9**: Select tile type in editor
