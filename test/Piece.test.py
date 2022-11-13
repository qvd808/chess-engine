import sys
parent_dir = sys.path[0].split('\\')

for i, file in enumerate(parent_dir):
    if file == "chess-engine":
        parent_dir = parent_dir[0:i+1]

sys.path.append("\\".join(parent_dir))

import unittest
from component.piece.Piece import Piece

# Piece should be able to get its postion

class PieceUnitTest(unittest.TestCase):

    def setUp(self) -> None:
        self.piece1 = Piece('H5', 'white')
        self.piece2 = Piece('A8', 'black')


    def test_Get_Position(self):
        self.assertEqual(self.piece1.col, 'H')
        self.assertEqual(self.piece1.row, '5')

        self.assertEqual(self.piece2.col, 'A')
        self.assertEqual(self.piece2.row, '8')

    def test_RaiseErrorIfLengthNotTwo(self):
        with self.assertRaises(ValueError):
            errorPiece = Piece('H58', 'white')

        with self.assertRaises(ValueError):
            errorPiece = Piece('8', 'black')

    def test_RaiseErrorIfValueIsNotValid(self):
        with self.assertRaises(ValueError):
            errorPiece = Piece('g5', 'white')

        with self.assertRaises(ValueError):
            errorPiece = Piece('8g', 'black')

        with self.assertRaises(ValueError):
            errorPiece = Piece('G5', 'red')

        with self.assertRaises(ValueError):
            errorPiece = Piece('C4', 'blue')
        
        with self.assertRaises(ValueError):
            errorPiece = Piece(32, 6)

        with self.assertRaises(ValueError):
            errorPiece = Piece(True, [])

    
    def test_Move_Piece(self):
        self.assertEqual(self.piece1.move('B5'), True)
        self.assertEqual(self.piece1.row, '5')
        self.assertEqual(self.piece1.col, 'B')

        self.assertEqual(self.piece1.move('B5'), False)
        self.assertEqual(self.piece1.row, '5')
        self.assertEqual(self.piece1.col, 'B')

        self.assertEqual(self.piece1.move('A5'), True)       
        self.assertEqual(self.piece1.row, '5')
        self.assertEqual(self.piece1.col, 'A')

        self.assertEqual(self.piece1.move('A5'), False)       
        self.assertEqual(self.piece1.row, '5')
        self.assertEqual(self.piece1.col, 'A')

    def test_RaiseErrorIfMove(self):
        with self.assertRaises(ValueError):
            self.piece1.move('g4')

        with self.assertRaises(ValueError):
            self.piece1.move('A10')

    def test_Get_Position(self):
        self.assertEqual(self.piece1.getPosition(), 'H5')
        self.assertEqual(self.piece2.getPosition(), 'A8')

    def test_getColor(self):
        self.assertEqual(self.piece1.color, 'white')
        self.assertEqual(self.piece2.color, 'black')


if __name__ == "__main__":
    unittest.main()
