import pygame
from .game_object import GameObject

# Physics constants
GRAVITY = 0.5
JUMP_POWER = -10
MOVE_SPEED = 4
TILE_SIZE = 32

class Player(GameObject):
    """Player controlled character."""

    def __init__(self, x, y):
        super().__init__(x, y, TILE_SIZE, TILE_SIZE, color=(0, 0, 255))
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.score = 0

    def handle_input(self):
        """Process keyboard input for movement."""
        keys = pygame.key.get_pressed()
        self.vel_x = 0
        if keys[pygame.K_LEFT]:
            self.vel_x = -MOVE_SPEED
        if keys[pygame.K_RIGHT]:
            self.vel_x = MOVE_SPEED
        if keys[pygame.K_UP] and self.on_ground:
            self.vel_y = JUMP_POWER
            self.on_ground = False

    def apply_gravity(self):
        """Apply gravity to the player."""
        self.vel_y += GRAVITY

    def horizontal_collisions(self, tiles):
        for tile in tiles:
            if tile.tile_type == '#':
                if self.rect.colliderect(tile.rect):
                    if self.vel_x > 0:
                        self.rect.right = tile.rect.left
                    elif self.vel_x < 0:
                        self.rect.left = tile.rect.right

    def vertical_collisions(self, tiles):
        self.on_ground = False
        for tile in tiles:
            if tile.tile_type == '#':
                if self.rect.colliderect(tile.rect):
                    if self.vel_y > 0:
                        self.rect.bottom = tile.rect.top
                        self.vel_y = 0
                        self.on_ground = True
                    elif self.vel_y < 0:
                        self.rect.top = tile.rect.bottom
                        self.vel_y = 0

    def update(self, tiles, enemies, items):
        """Update the player position and handle interactions."""
        self.handle_input()
        self.apply_gravity()
        # Horizontal movement
        self.rect.x += self.vel_x
        self.horizontal_collisions(tiles)
        # Vertical movement
        self.rect.y += self.vel_y
        self.vertical_collisions(tiles)
        # Item collection
        for item in items[:]:
            if self.rect.colliderect(item.rect):
                if item.item_type == 'coin':
                    self.score += 1
                items.remove(item)
        # Enemy interaction
        for enemy in enemies[:]:
            if self.rect.colliderect(enemy.rect):
                if self.vel_y > 0 and self.rect.bottom - enemy.rect.top < 20:
                    enemies.remove(enemy)
                    self.vel_y = JUMP_POWER / 2
                else:
                    # Simple death -> reset score and position
                    self.rect.topleft = (0, 0)
                    self.score = 0
