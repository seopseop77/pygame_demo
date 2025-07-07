import pygame
from .game_object import GameObject
from .projectile import Projectile

# Physics constants
GRAVITY = 0.5
JUMP_POWER = -10
MOVE_SPEED = 4
TILE_SIZE = 32

class Player(GameObject):
    """Player controlled character."""

    def __init__(self, x, y):
        super().__init__(x, y, TILE_SIZE, TILE_SIZE, color=(0, 0, 255))
        self.spawn = (x, y)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        self.score = 0
        self.move_speed = MOVE_SPEED
        self.invincible_until = 0
        self.can_shoot = False
        self.last_shot = 0
        self.deaths = 0
        self.enemies_killed = 0
        self.start_time = 0
        self.end_time = 0
        self.direction = 1

    def handle_input(self):
        """Process keyboard input for movement."""
        keys = pygame.key.get_pressed()
        self.vel_x = 0
        if keys[pygame.K_LEFT]:
            self.vel_x = -self.move_speed
            self.direction = -1
        if keys[pygame.K_RIGHT]:
            self.vel_x = self.move_speed
            self.direction = 1
        if keys[pygame.K_UP] and self.on_ground:
            self.vel_y = JUMP_POWER
            self.on_ground = False

    def shoot(self, projectiles):
        if self.can_shoot:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_shot > 300:
                    proj = Projectile(self.rect.centerx, self.rect.centery, self.direction)
                    projectiles.append(proj)
                    self.last_shot = current_time

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

    def update(self, tiles, enemies, items, projectiles):
        """Update the player position and handle interactions."""
        self.handle_input()
        self.apply_gravity()
        self.shoot(projectiles)
        # Horizontal movement
        self.rect.x += self.vel_x
        self.horizontal_collisions(tiles)
        # Vertical movement
        self.rect.y += self.vel_y
        self.vertical_collisions(tiles)
        # Item collection
        current_time = pygame.time.get_ticks()
        for item in items[:]:
            if self.rect.colliderect(item.rect):
                if item.item_type == 'coin':
                    self.score += 1
                elif item.item_type == 'speed':
                    self.move_speed += 2
                elif item.item_type == 'invincibility':
                    self.invincible_until = current_time + 5000
                elif item.item_type == 'projectile':
                    self.can_shoot = True
                items.remove(item)
        # Enemy interaction
        for enemy in enemies[:]:
            if self.rect.colliderect(enemy.rect):
                if self.vel_y > 0 and self.rect.bottom - enemy.rect.top < 20:
                    enemies.remove(enemy)
                    self.enemies_killed += 1
                    self.vel_y = JUMP_POWER / 2
                else:
                    if current_time > self.invincible_until:
                        self.rect.topleft = self.spawn
                        self.vel_x = self.vel_y = 0
                        self.deaths += 1
                    else:
                        enemies.remove(enemy)
