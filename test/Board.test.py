import sys
parent_dir = sys.path[0].split('\\')

for i, file in enumerate(parent_dir):
    if file == "chess-engine":
        parent_dir = parent_dir[0:i+1]

sys.path.append("\\".join(parent_dir))

import unittest
from component.Board import Board
from component.piece.Piece import Piece

# Board should get the postion of the chess piece
# Board should only need to know if a position is occupy or not
# You should be able to insert a chess piece into a position
# Board should be able to render itself or another class should do the render job
# 

class boardUniTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.board = Board()

    def test_Insert_Piece(self):
        piece1 = Piece('A5', 'white')
        expectation = [8 * [0]] * 8
        expectation[0][4] = piece1
        self.assertTrue(self.board.insert(piece1))
        self.assertEqual(self.board.board, expectation)

        piece2 = Piece('A5', 'black')
        self.assertFalse(self.board.insert(piece2))
        self.assertEqual(self.board.board, expectation)

        piece3 = Piece('B4', 'white')
        expectation[1][3] = piece3
        self.assertTrue(self.board.insert(piece3))
        self.assertEqual(self.board.board, expectation)
    
    def test_IsThereAPiece(self):
        piece1 = Piece('H5', 'white')
        self.board.insert(piece1)
        self.assertTrue(self.board.isOccupy('H5'))
        self.assertFalse(self.board.isOccupy('B4'))

        piece2 = Piece('A8', 'black')
        self.board.insert(piece2)
        self.assertTrue(self.board.isOccupy('A8'))
        self.assertFalse(self.board.isOccupy('H4'))


    def test_RaisePieceError(self):
        with self.assertRaises(ValueError):
            self.board.insert([])

        with self.assertRaises(ValueError):
            self.board.insert("")

    def test_RaisePositionErrorForIsOccupy(self):
        piece1 = Piece('H5', 'white')
        self.board.insert(piece1)
        with self.assertRaises(ValueError):
            self.board.isOccupy(4)

        piece2 = Piece('A8', 'black')
        self.board.insert(piece2)

        with self.assertRaises(ValueError):
            self.board.isOccupy('2345234')




if __name__ == "__main__":
    unittest.main()
