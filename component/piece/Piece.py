class Piece():
    def __init__(self, position) -> None:

        self.RaisePositionError(position)

        self.col = position[0]
        self.row = position[1]
    
    def move(self, new_position) -> bool:

        self.RaisePositionError(new_position)

        if new_position[0] == self.col and new_position[1] == self.row:
            return False
        else:
            self.col = new_position[0]
            self.row = new_position[1]

            return True


    def RaisePositionError(self, position):
        if len(position) != 2:
            raise ValueError("Length of position should be two")

        if  not '1' <= position[1] <= '8':
            raise ValueError("Invalid input for the row")

        if  not 'A' <= position[0] <= 'H':
            raise ValueError("Invalid input for the column")

    def getPosition(self) -> str:
        return self.col + self.row
