import os
import sys
"""Entry point for the platformer game."""
from game.game import Game


def main():
    """Run the game with the selected map."""
    map_name = sys.argv[1] if len(sys.argv) > 1 else "level1.txt"
    map_path = os.path.join(os.path.dirname(__file__), "maps", map_name)
    game = Game(map_path)
    game.run()


if __name__ == "__main__":
    main()
