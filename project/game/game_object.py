import pygame

class GameObject:
    """Base class for all game objects."""

    def __init__(self, x, y, width, height, color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = None
        self.color = color

    def draw(self, screen):
        """Draw the object to the screen."""
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

    def update(self, tiles):
        """Update the object. To be overridden by subclasses."""
        pass
