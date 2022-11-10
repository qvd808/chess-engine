import pygame

class Display():
    def __init__(self, width = 800, height = 600) -> None:
        pygame.init()

        self.width = width
        self.height = height

    def turnOffDisplayOnExitButton(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def runDisplay(self):
        pygame.display.init()
        pygame.display.set_mode(size = (self.width, self.height))

        while True:

            self.turnOffDisplayOnExitButton()

            pygame.display.update()