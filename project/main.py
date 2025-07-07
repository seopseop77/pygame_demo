import os
"""Entry point for the platformer game."""
from game.game import Game


def main():
    game = Game(os.path.join(os.path.dirname(__file__), "maps", "level1.txt"))
    game.run()


if __name__ == "__main__":
    main()
