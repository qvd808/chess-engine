
import sys
parent_dir = sys.path[0].split('\\')

for i, file in enumerate(parent_dir):
    if file == "chess-engine":
        parent_dir = parent_dir[0:i+1]

sys.path.append("\\".join(parent_dir))

from utils.ErrorHandling import ErrorHandling

####################################################

class Piece():
    def __init__(self, position, color) -> None:

        self.error = ErrorHandling()

        self.error.RaisePositionError(position)
        self.error.RaiseColorError(color)

        self.col = position[0]
        self.row = position[1]

        self.color = color
    
    def move(self, new_position) -> bool:

        self.error.RaisePositionError(new_position)

        if new_position[0] == self.col and new_position[1] == self.row:
            return False
        else:
            self.col = new_position[0]
            self.row = new_position[1]

            return True

    def getPosition(self) -> str:
        return self.col + self.row
