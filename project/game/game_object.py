import pygame

class GameObject:
    """Base class for all game objects."""

    def __init__(self, x, y, width, height, color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = None
        self.color = color

    def draw(self, screen, camera_x=0):
        """Draw the object to the screen taking camera offset into account."""
        draw_rect = self.rect.move(-camera_x, 0)
        if self.image:
            screen.blit(self.image, draw_rect)
        else:
            pygame.draw.rect(screen, self.color, draw_rect)

    def update(self, tiles):
        """Update the object. To be overridden by subclasses."""
        pass
