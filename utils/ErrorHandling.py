class ErrorHandling:
    def __init__(self) -> None:
        pass
    
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