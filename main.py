from utils.display import Display

class MainGame ():
    def __init__(self) -> None:
        self.display = Display()
    
    def run(self):
        self.display.runDisplay()



if __name__ == "__main__":
    game = MainGame()
    game.run()
