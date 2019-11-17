

#Importing an object Cell, in order to use the object functions and attributes here
from cell import Cell

# Creating a Column object, containing information about column of the board, such as cell objects in the column
class Column:


    def __init__(self, col):
        '''Defining class attributes here'''

        # Object col shows the position number of the each cell stored in column
        self.col = col

        # Creating an list to store cell objects 
        self.column_list = []

        # Creates position number to create cell objects in order, in total 6 of them
        for i in range(6):

            # For each i position, create a cell object accordingly
            self.column_list.append(Cell(i, col))
        
        
