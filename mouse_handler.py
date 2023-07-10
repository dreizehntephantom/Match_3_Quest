import pygame


class MouseHandler:
    def __init__(self):
        self.mouse_button_down = False
        self.mouse_position = (0, 0)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_down = False

        self.mouse_position = pygame.mouse.get_pos()

    def is_mouse_button_down(self):
        return self.mouse_button_down

    def get_mouse_position(self):
        return self.mouse_position
