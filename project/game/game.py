"""Core game loop and state management."""
import pygame

from editor.map_loader import load_map
from editor.map_editor import MapEditor
from game.projectile import Projectile

TILE_SIZE = 32
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Game:
    """Main game class handling game loop.

    Screen size is fixed at 640x480 and the camera follows the player when
    the map is wider than the screen.
    """

    def __init__(self, map_file: str):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Platformer")
        self.clock = pygame.time.Clock()
        self.map_file = map_file

        # Load level
        self.load_world()
        self.running = True
        self.camera_x = 0
        self.projectiles = []

    def load_world(self):
        """Load game objects from map file."""
        data = load_map(self.map_file)
        self.map_data, self.player, self.tiles, self.enemies, self.items = data
        self.map_width = len(self.map_data[0]) * TILE_SIZE if self.map_data else SCREEN_WIDTH
        self.fix_overlaps()

    def fix_overlaps(self):
        """Move objects out of wall tiles if they overlap when loaded."""
        solids = [t for t in self.tiles if t.tile_type == '#']
        for obj in [self.player, *self.enemies, *self.items]:
            for tile in solids:
                if obj.rect.colliderect(tile.rect):
                    obj.rect.bottom = tile.rect.top

    def run(self):
        """Main loop for the game."""
        self.player.start_time = pygame.time.get_ticks()
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    editor = MapEditor(self.screen, self.map_data, self.map_file)
                    self.map_data = editor.run()
                    self.load_world()
            # Update objects
            self.player.update(
                self.tiles,
                self.enemies,
                self.items,
                self.projectiles,
                self.map_width,
            )
            for enemy in self.enemies:
                enemy.update(self.tiles)
            for projectile in self.projectiles[:]:
                projectile.update()
                remove = False
                for tile in self.tiles:
                    if tile.tile_type == '#':
                        if projectile.rect.colliderect(tile.rect):
                            remove = True
                            break
                if remove:
                    self.projectiles.remove(projectile)
                    continue
                for enemy in self.enemies[:]:
                    if projectile.rect.colliderect(enemy.rect):
                        self.enemies.remove(enemy)
                        self.projectiles.remove(projectile)
                        self.player.enemies_killed += 1
                        break

            # Update camera position
            self.camera_x = max(
                0,
                min(
                    self.player.rect.centerx - SCREEN_WIDTH // 2,
                    self.map_width - SCREEN_WIDTH,
                ),
            )

            # Goal check
            for tile in self.tiles:
                if tile.tile_type == 'E' and self.player.rect.colliderect(tile.rect):
                    self.player.end_time = pygame.time.get_ticks()
                    self.running = False
                    break
            # Draw
            self.draw()
            pygame.display.flip()
        self.show_final_score()
        pygame.quit()

    def draw(self):
        self.screen.fill((135, 206, 235))
        for tile in self.tiles:
            tile.draw(self.screen, self.camera_x)
        for item in self.items:
            item.draw(self.screen, self.camera_x)
        for enemy in self.enemies:
            enemy.draw(self.screen, self.camera_x)
        for projectile in self.projectiles:
            projectile.draw(self.screen, self.camera_x)
        self.player.draw(self.screen, self.camera_x)
        self.draw_ui()

    def draw_ui(self):
        font = pygame.font.SysFont(None, 24)
        text = font.render(f"Score: {self.player.score}", True, (0, 0, 0))
        self.screen.blit(text, (10, 10))
        status_y = 30
        if pygame.time.get_ticks() < self.player.invincible_until:
            inv = font.render("INVINCIBLE", True, (255, 0, 0))
            self.screen.blit(inv, (10, status_y))
            status_y += 20
        if self.player.can_shoot:
            shoot = font.render("CAN SHOOT", True, (0, 0, 0))
            self.screen.blit(shoot, (10, status_y))

    def show_final_score(self):
        time_taken = (self.player.end_time - self.player.start_time) / 1000
        enemies_score = self.player.enemies_killed * 100
        final_score = enemies_score - (self.player.deaths * 100) - (time_taken * 2)
        print(f"Final Score: {int(final_score)}")

