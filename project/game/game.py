"""Core game loop and state management."""
import pygame

from editor.map_loader import load_map
from editor.map_editor import MapEditor

TILE_SIZE = 32
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Game:
    """Main game class handling game loop."""

    def __init__(self, map_file: str):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Platformer")
        self.clock = pygame.time.Clock()
        self.map_file = map_file

        # Load level
        self.load_world()
        self.running = True

    def load_world(self):
        """Load game objects from map file."""
        data = load_map(self.map_file)
        self.map_data, self.player, self.tiles, self.enemies, self.items = data

    def run(self):
        """Main loop for the game."""
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
            self.player.update(self.tiles, self.enemies, self.items)
            for enemy in self.enemies:
                enemy.update(self.tiles)
            # Draw
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        self.screen.fill((135, 206, 235))
        for tile in self.tiles:
            tile.draw(self.screen)
        for item in self.items:
            item.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        self.player.draw(self.screen)
        self.draw_ui()

    def draw_ui(self):
        font = pygame.font.SysFont(None, 24)
        text = font.render(f"Score: {self.player.score}", True, (0, 0, 0))
        self.screen.blit(text, (10, 10))
