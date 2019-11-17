

#Creating an object for the cell; cell contains the information of the each position in the board, 
class Cell:


    def __init__(self, row, col):
        '''Defining the class attributes here'''

        # This attribute shows if the position is empty
        self.hold = None

        # Row attribute defines the row number of the position
        self.row = row

        # Col attribute defines teh column number of the position
        self.col = col
