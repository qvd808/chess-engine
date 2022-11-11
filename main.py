from utils.display import Display
import pygame

class MainGame ():
    def __init__(self) -> None:
        pygame.init()
        self.display = Display()
    
    def run(self):
        self.display.runDisplay()

        while True:

            self.display.turnOffDisplayOnExitButton()

            self.display.runDisplayUpdate()



if __name__ == "__main__":
    game = MainGame()
    game.run()
