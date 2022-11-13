import pygame

# Display should only worries about how to display something on the screen, it should not care about render or other method that it need to worries about

class Render():
    def __init__(self) -> None:
        self.draw = pygame.draw

    def draw_board(self, surface):

        self.draw.rect(surface, (255,255,255), (200, 200, 100, 100), 1)

class Display():
    def __init__(self, width = 800, height = 600) -> None:
        pygame.init()

        self.width = width
        self.height = height
        self.surface = None

        self.render = Render()

    def turnOffDisplayOnExitButton(self, exit_game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

    def draw_board(self):
        self.render.draw_board(self.surface)

    def runDisplayUpdate(self):
        pygame.display.update()

    def runDisplay(self):
        pygame.display.init()
        self.surface = pygame.display.set_mode(size = (self.width, self.height))
