class BoardCordinateToIndex:
    def __init__(self)->None:
        pass
    
    def getCordinate(self, position):
        x = position[0]
        y = position[1]
        x = ord(x) - ord('A')
        y = ord(y) - ord('1')
        return (x, y)

class Board:
    def __init__(self) -> None:
        self.board = [[0] * 8] * 8
        self.__coordinate = BoardCordinateToIndex()
    
    def insert(self, piece) -> bool:
        position = piece.getPosition()
        xCor, yCor = self.__coordinate.getCordinate(position)

        if (self.isOccupy(position)):
            return False
        else:
            self.board[xCor][yCor] = piece
            return True
    
    def isOccupy(self, position) -> bool:
        xCor, yCor = self.__coordinate.getCordinate(position)
        return self.board[xCor][yCor] != 0