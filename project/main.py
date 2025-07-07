import os
import sys
"""Entry point for the platformer game."""
import pygame
from game.game import Game
from config import SCREEN_WIDTH, SCREEN_HEIGHT, COLORS


def show_help(screen):
    font = pygame.font.SysFont(None, 24)
    running = True
    lines = [
        "Left/Right: Move",
        "Up: Jump",
        "Space: Shoot (with item)",
        "Reach the green tile to win",
    ]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
        screen.fill(COLORS["background"])
        for i, line in enumerate(lines):
            text = font.render(line, True, (0, 0, 0))
            screen.blit(text, (40, 40 + i * 30))
        prompt = font.render("Press SPACE to return", True, (0, 0, 0))
        screen.blit(prompt, (40, 40 + len(lines) * 30 + 20))
        pygame.display.flip()


def show_start(screen):
    font = pygame.font.SysFont(None, 36)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                if event.key == pygame.K_h:
                    show_help(screen)
        screen.fill(COLORS["background"])
        text = font.render("SPACE: Start  H: Help", True, (0, 0, 0))
        rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, rect)
        pygame.display.flip()


def main():
    """Run the game with the selected map."""
    map_name = sys.argv[1] if len(sys.argv) > 1 else "level1.txt"
    map_path = os.path.join(os.path.dirname(__file__), "maps", map_name)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    show_start(screen)
    game = Game(map_path, screen)
    game.run()


if __name__ == "__main__":
    main()
