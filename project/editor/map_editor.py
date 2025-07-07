"""Simple map editor accessible during the game."""
import pygame
from typing import List

from .map_loader import save_map
from game.tile import TILE_SIZE

COLOR_LOOKUP = {
    '.': (0, 0, 0),
    '#': (100, 100, 100),
    'P': (0, 0, 255),
    'G': (255, 0, 0),
    'C': (255, 215, 0),
}

TILE_TYPES = ['.', '#', 'P', 'G', 'C']

class MapEditor:
    """Interactive tile-based map editor."""

    def __init__(self, screen: pygame.Surface, map_data: List[List[str]], file_path: str):
        self.screen = screen
        self.map_data = map_data
        self.file_path = file_path
        self.selected = '#'
        self.font = pygame.font.SysFont(None, 24)

    def run(self) -> List[List[str]]:
        """Run the editor loop until the user exits."""
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_s:
                        save_map(self.file_path, self.map_data)
                    elif event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5):
                        index = event.key - pygame.K_1
                        self.selected = TILE_TYPES[index]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    grid_x = mx // TILE_SIZE
                    grid_y = my // TILE_SIZE
                    if 0 <= grid_y < len(self.map_data) and 0 <= grid_x < len(self.map_data[0]):
                        if event.button == 1:
                            self.map_data[grid_y][grid_x] = self.selected
                        elif event.button == 3:
                            self.map_data[grid_y][grid_x] = '.'

            self.draw()
            pygame.display.flip()
        # Return updated map
        return self.map_data

    def draw(self):
        self.screen.fill((0, 0, 0))
        for y, row in enumerate(self.map_data):
            for x, char in enumerate(row):
                color = COLOR_LOOKUP.get(char, (255, 255, 255))
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (40, 40, 40), rect, 1)
        text = self.font.render(f"Selected: {self.selected} | S: Save | ESC: Exit", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))
