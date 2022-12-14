class ErrorHandling:
    def __init__(self) -> None:
        pass
    
    def RaisePositionError(self, position) -> None:
        if not isinstance(position, str):
            raise ValueError("Value must be a string")

        if len(position) != 2:
            raise ValueError("Length of position should be two")

        if  not '1' <= position[1] <= '8':
            raise ValueError("Invalid input for the row")

        if  not 'A' <= position[0] <= 'H':
            raise ValueError("Invalid input for the column")

    def RaiseColorError(self, color) -> None:
        if not isinstance(color, str):
            raise ValueError("Value must be a string")
        
        if color != 'white' and color != 'black':
            raise ValueError("Value must be a string that is 'white' or 'black'")

    def RaisePieceError(self, piece, type) -> None:
        if not isinstance(piece, type):
            raise ValueError("Value must be a Piece object")