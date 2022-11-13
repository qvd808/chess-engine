import pygame

# Display should only worries about how to display something on the screen, it should not care about render or other method that it need to worries about
# Render should not worried about calculating the coordinate and should leave it to another classes

class Display():
    def __init__(self, width = 800, height = 600) -> None:
        pygame.init()

        self.width = width
        self.height = height

        self.render = Render(self)

    def turnOffDisplayOnExitButton(self, exit_game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

    def draw_board(self):
        self.render.draw_board(self)

    def runDisplayUpdate(self):
        pygame.display.update()

    def runDisplay(self):
        pygame.display.init()
        self.surface = pygame.display.set_mode(size = (self.width, self.height))


class Render():
    def __init__(self, display:Display) -> None:
        self.draw = pygame.draw
        self.WHITE = (255, 255, 255)
        self.BROWN = (165, 42, 42)

        self.__coorCalculator = CoordinateCalculator(display)


    def draw_board(self, display: Display):

        xCor, yCor, width = self.__coorCalculator.boardCordinate(display)
        surface = display.surface

        self.draw.rect(surface, self.BROWN, (xCor, yCor, width, width), 1)

        for i in range(8):
            for j in range(4):
                if i % 2 == 0:
                    self.draw.rect(surface, self.WHITE, (xCor + width//4 * j, yCor + width//8 * i, width//8, width//8))
                else:
                    self.draw.rect(surface, self.WHITE, ((xCor + width//8) + width//4 * j, yCor + width//8 * i, width//8, width//8))
        

class CoordinateCalculator:
    def __init__(self, display:Display) -> None:
        self.board_area_percentage = 60

    def boardCordinate(self, display: Display):

        width = int(self.board_area_percentage * display.width // 100)
        x = int(display.width // 2 - width // 2)
        y = int(display.height // 2 - width // 2)

        return (x, y, width)
    

