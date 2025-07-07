import os
import sys
import pygame

from editor.map_loader import load_map
from editor.map_editor import MapEditor
from config import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    map_name = sys.argv[1] if len(sys.argv) > 1 else "level1.txt"
    map_path = os.path.join(os.path.dirname(__file__), "maps", map_name)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    map_data, *_ = load_map(map_path)
    editor = MapEditor(screen, map_data, map_path)
    editor.run()
    pygame.quit()


if __name__ == "__main__":
    main()
