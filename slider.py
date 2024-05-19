import pygame

SLIDER_COLOR = (200, 200, 200)
HANDLE_COLOR = (219, 34, 34)

class Slider:
    def __init__(self, x, y, width, height, min_val, max_val, start_val):
        self.rect = pygame.Rect(x, y, width, height)
        self.handle_rect = pygame.Rect(x, y, height, height)
        self.min_val = min_val
        self.max_val = max_val
        self.value = start_val
        self.handle_pos = x + ((start_val - min_val) / (max_val - min_val)) * (width - height)
        self.dragging = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.handle_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.handle_pos = max(self.rect.x, min(event.pos[0] - self.handle_rect.width / 2, self.rect.x + self.rect.width - self.handle_rect.width))
                self.value = self.min_val + (self.handle_pos - self.rect.x) / (self.rect.width - self.handle_rect.width) * (self.max_val - self.min_val)

    def draw(self, screen):
        pygame.draw.rect(screen, SLIDER_COLOR, self.rect)
        self.handle_rect.x = self.handle_pos
        pygame.draw.rect(screen, HANDLE_COLOR, self.handle_rect)

    def get_value(self):
        return self.value