class Piece():
    def __init__(self, position, color) -> None:

        self.RaisePositionError(position)
        self.RaiseColorError(color)

        self.col = position[0]
        self.row = position[1]

        self.color = color
    
    def move(self, new_position) -> bool:

        self.RaisePositionError(new_position)

        if new_position[0] == self.col and new_position[1] == self.row:
            return False
        else:
            self.col = new_position[0]
            self.row = new_position[1]

            return True


    def RaisePositionError(self, position):
        if not isinstance(position, str):
            raise ValueError("Value must be a string")

        if len(position) != 2:
            raise ValueError("Length of position should be two")

        if  not '1' <= position[1] <= '8':
            raise ValueError("Invalid input for the row")

        if  not 'A' <= position[0] <= 'H':
            raise ValueError("Invalid input for the column")

    def RaiseColorError(self, color):
        if not isinstance(color, str):
            raise ValueError("Value must be a string")
        
        if color != 'white' and color != 'black':
            raise ValueError("Value must be a string that is 'white' or 'black'")

    def getPosition(self) -> str:
        return self.col + self.row
