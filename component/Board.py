import sys
parent_dir = sys.path[0].split('\\')

for i, file in enumerate(parent_dir):
    if file == "chess-engine":
        parent_dir = parent_dir[0:i+1]

sys.path.append("\\".join(parent_dir))

from utils.ErrorHandling import ErrorHandling

####################################################

class BoardCordinateToIndex:
    def __init__(self)->None:
        
        self.error = ErrorHandling()
    
    def getCordinate(self, position):
        self.error.RaisePositionError(position)

        x = position[0]
        y = position[1]
        x = ord(x) - ord('A')
        y = ord(y) - ord('1')
        return (x, y)

class Board:
    def __init__(self) -> None:
        self.board = [[0] * 8] * 8
        self.__coordinate = BoardCordinateToIndex()
        self.error = ErrorHandling()
    
    def insert(self, piece) -> bool:
        position = piece.getPosition()
        xCor, yCor = self.__coordinate.getCordinate(position)

        if (self.isOccupy(position)):
            return False
        else:
            self.board[xCor][yCor] = piece
            return True
    
    def isOccupy(self, position) -> bool:
        self.error.RaisePositionError(position)

        xCor, yCor = self.__coordinate.getCordinate(position)
        return self.board[xCor][yCor] != 0
