import unittest
from Piece import Piece

# Piece should be able to get its postion

class PieceUnitTest(unittest.TestCase):

    def setUp(self) -> None:
        self.piece1 = Piece('H5')
        self.piece2 = Piece('A8')


    def test_Get_Position(self):
        self.assertEqual(self.piece1.col, 'H')
        self.assertEqual(self.piece1.row, '5')

        self.assertEqual(self.piece2.col, 'A')
        self.assertEqual(self.piece2.row, '8')

    def test_RaiseErrorIfLengthNotTwo(self):
        with self.assertRaises(ValueError):
            errorPiece = Piece('H58')

        with self.assertRaises(ValueError):
            errorPiece = Piece('8')

    def test_RaiseErrorIfValueIsNotValid(self):
        with self.assertRaises(ValueError):
            errorPiece = Piece('g5')

        with self.assertRaises(ValueError):
            errorPiece = Piece('8g')

    
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


if __name__ == "__main__":
    unittest.main()
