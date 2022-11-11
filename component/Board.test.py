import unittest
from Board import Board

# Board should get the postion of the chess piece
# You should be able to insert a chess piece into a position
# Board should be able to render itself or another class should do the render job
# 

class boardUniTest(unittest.TestCase):
    def test_Get_Board_Position(self):
        board = Board()
    
    def test_Insert_Piece(self):
        pass


if __name__ == "__main__":
    unittest.main()