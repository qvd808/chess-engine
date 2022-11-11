import pygame

# Display should only worries about how to display something on the screen, it should not care about render or other method that it need to worries about

class Display():
    def __init__(self, width = 800, height = 600) -> None:
        pygame.init()

        self.width = width
        self.height = height

    def turnOffDisplayOnExitButton(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def runDisplayUpdate(self):
        pygame.display.update()

    def runDisplay(self):
        pygame.display.init()
        pygame.display.set_mode(size = (self.width, self.height))
