from utils.Display import Display
import pygame

class MainGame ():
    def __init__(self) -> None:
        pygame.init()
        self.display = Display()

        self.running = True
    
    def run(self):
        self.display.runDisplay()

        while self.running:

            self.display.turnOffDisplayOnExitButton(self.exit_game)

            self.display.draw_board()

            self.display.runDisplayUpdate()

    def exit_game(self):
        self.running = False



if __name__ == "__main__":
    game = MainGame()
    game.run()
