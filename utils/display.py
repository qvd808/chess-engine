import pygame
from utils.Render import Render

# Display should only worries about how to display something on the screen, it should not care about render or other method that it need to worries about

class Display():
    def __init__(self, width = 800, height = 600) -> None:
        pygame.init()

        self.width = width
        self.height = height

        self.render = Render()

    def turnOffDisplayOnExitButton(self, exit_game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

    def runDisplayUpdate(self):
        pygame.display.update()

    def runDisplay(self):
        pygame.display.init()
        pygame.display.set_mode(size = (self.width, self.height))
