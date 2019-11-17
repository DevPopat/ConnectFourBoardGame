

#Importing an object column, in order to use its attributes and functions
from column import Column

#Importing an object chip, in order to use its attributes and functions
from chip import Chip

#Creating a Board object, containing information about whole board- which includes the game board and cells in the board
class Board:
     

    def __init__(self):
        '''Defining the class attributes here'''

        #In case the user makes an invalid move, the error attribute will show the user direction to do it again.
        self.error = "\nThis is an invalid move. Look at the board carefully and play again.\n"

        #Board_full attribute shows if the board is completely full or not.
        self.board_full = False

        #Creating a list in order to store board data
        self.board_list = []

        #Creating 7 positions to create the row of the board
        for i in range(7):

            #Storing the column information into the board list
            self.board_list.append(Column(i))

        #Winner attribute shows if there is a winner in the game or not
        self.winner = False

        #Chip_color attribute shows whose turn it is at the moment, default is red, meaning the player with red chips will start making move first.
        self.chip_color = 'R'

        #Creating a base board to begin with
        self.output_list = [
            
                           ['.','.','.','.','.','.'],
                           ['.','.','.','.','.','.'],
                           ['.','.','.','.','.','.'],
                           ['.','.','.','.','.','.'],
                           ['.','.','.','.','.','.'],
                           ['.','.','.','.','.','.'],
                           ['.','.','.','.','.','.']
                           
                           ]
        
        
    
    def make_move(self, col_number):
        '''stores the chips into the proper position of the board'''

        #Creating a counter value that counts number of chips in the specified column
        not_full = 0

        #Going through the column, in order to check each cell value
        for i in range(len(self.board_list[0].column_list)-1,-1,-1):

            #Checking if the certain position is empty
            if self.board_list[col_number].column_list[i].hold == None:

                #If the position is empty, drop the chip into that position
                self.board_list[col_number].column_list[i].hold = Chip(str(self.chip_color))

                #Once this is done, break out of the for loop
                break

            #When if statement passes, moving onto else statement
            else:

                #Adding a number to the counter value not_full to count how many chips are filled in the column
                not_full = not_full + 1

        #Checking if the player is making invalid move, such as trying to drop the chip onto the column that is already full       
        if not_full == 6:

            #Return the message to the game in order to inform the player to make different move
            return self.error
       
            
    def whose_turn(self):
        '''changes the current turn of the game'''

        #Checking if the previous player was red
        if self.chip_color == 'R':

            #Changing the current player to yellow, indicating that it is player yellow's turn
            self.chip_color = 'Y'

        #Checking if the previous player was yellow
        elif self.chip_color == 'Y':

            #Changing the current player to red, indicating that it is player red's turn
            self.chip_color = 'R'
            
    #Defining a function that will return whose turn it is
    def get_chip_color(self):
        '''Return whose turn it is'''

        #Return attribute chip_color of the object
        return self.chip_color


    def vertical_win(self):
        '''Checks for the vertical match of the chips'''

        #Checking each column of the board
        for i in range(len(self.board_list)):

            #Checking each cell value of the column
            for j in range(len(self.board_list[i].column_list)):

                #Checking if the row position number of the cell is less than or equal to 3
                if j <= 2:

                    #Checking if the cell and 3 cells below itself are not empty and each contains the chip.
                    if (self.board_list[i].column_list[j].hold
                        and self.board_list[i].column_list[j + 1].hold
                        and self.board_list[i].column_list[j + 2].hold 
                        and self.board_list[i].column_list[j + 3].hold):

                        #Checking if the cell has matching color with the cells below itself
                        if (self.board_list[i].column_list[j].hold.color 
                           ==  self.board_list[i].column_list[j + 1].hold.color 
                           == self.board_list[i].column_list[j + 2].hold.color 
                           == self.board_list[i].column_list[j + 3].hold.color):

                            #Switching the winner attribute value to true, indicating that there is a winner in the game
                            self.winner = True
        

    def horizontal_win(self):
        '''Checks for the horizontal match of the chips'''

        #Checking each column of the board
        for i in range(len(self.board_list)):

            #Checking each cell value of the column
            for j in range(len(self.board_list[i].column_list)):

                #Checking if the column position number of the cell is less than or equal to 4
                if i <= 3:

                    #Checking if the cell and 3 cells next to itself on the right are not empty and each contains the chip.
                    if (self.board_list[i].column_list[j].hold
                        and self.board_list[i + 1].column_list[j].hold
                        and self.board_list[i + 2].column_list[j].hold
                        and self.board_list[i + 3].column_list[j].hold):

                        #Checking if the cell has matching color with the cells next to itself on the right
                        if (self.board_list[i].column_list[j].hold.color 
                            ==  self.board_list[i + 1].column_list[j].hold.color 
                            == self.board_list[i + 2].column_list[j].hold.color 
                            == self.board_list[i + 3].column_list[j].hold.color):

                            #Switching the winner attribute value to true, indicating that there is a winner in the game
                            self.winner = True
        

    def diagonal_win(self):
        '''Checks for the diagonal match of the chips'''

        #Checking each column of the board
        for i in range(len(self.board_list)):

            #Checking each cell value of the column
            for j in range(len(self.board_list[0].column_list)):

                #Checking if the column position number of the cell is less than or equal to 4, AND if the row position number of the cell is less than or equal to 3
                if i<=3 and j<=2:

                    #Checking if the cell and 3 cells diagonally down to the right to itself are not empty and each contains the chip.
                    if (self.board_list[i].column_list[j].hold 
                        and self.board_list[i + 1].column_list[j + 1].hold 
                        and self.board_list[i + 2].column_list[j + 2].hold
                        and self.board_list[i + 3].column_list[j + 3].hold):

                        #Checking if the cell and 3 cells diagonally down to the right to itself are matching colors
                        if (self.board_list[i].column_list[j].hold.color 
                           ==  self.board_list[i + 1].column_list[j + 1].hold.color 
                           == self.board_list[i + 2].column_list[j + 2].hold.color 
                           == self.board_list[i + 3].column_list[j + 3].hold.color):

                            #Switching the winner attribute value to true, indicating that there is a winner in the game
                            self.winner = True

                    #Checking if the cell and 3 cells diagonally up to the right to itself are not empty and each contains the chip.
                    if (self.board_list[i].column_list[j].hold 
                       and self.board_list[i - 1].column_list[j + 1].hold 
                       and self.board_list[i - 2].column_list[j + 2].hold
                       and self.board_list[i - 3].column_list[j + 3].hold):

                        #Checking if the cell and 3 cells diagonally up to the right to itself are matching colors
                        if (self.board_list[i].column_list[j].hold.color 
                            ==  self.board_list[i - 1].column_list[j + 1].hold.color 
                            == self.board_list[i - 2].column_list[j + 2].hold.color 
                            == self.board_list[i - 3].column_list[j + 3].hold.color):

                            #Switching the winner attribute value to true, indicating that there is a winner in the game
                            self.winner = True

                            
                #Checking if the column position number of the cell is less than or equal to 4, AND if the row position number of the cell is greater than 3
                elif i<=3 and j>2:

                    #Checking if the cell and 3 cells diagonally down to the left to itself are not empty and each contains the chip.
                    if (self.board_list[i].column_list[j].hold
                         and self.board_list[i + 1].column_list[j -1].hold
                         and self.board_list[i + 2].column_list[j - 2].hold
                         and self.board_list[i + 3].column_list[j - 3].hold):

                        #Checking if the cell and 3 cells diagonally down to the left to itself are matching colors
                        if (self.board_list[i].column_list[j].hold.color 
                           ==  self.board_list[i + 1].column_list[j - 1].hold.color 
                           == self.board_list[i + 2].column_list[j - 2].hold.color 
                           == self.board_list[i + 3].column_list[j - 3].hold.color):

                            #Switching the winner attribute value to true, indicating that there is a winner in the game
                            self.winner = True
                    
                    #Checking if the cell and 3 cells diagonally up to the left to itself are not empty and each contains the chip.
                    if (self.board_list[i].column_list[j].hold
                       and self.board_list[i - 1].column_list[j -1].hold
                       and self.board_list[i - 2].column_list[j - 2].hold
                       and self.board_list[i - 3].column_list[j - 3].hold):

                        #Checking if the cell and 3 cells diagonally up to the left to itself are matching colors
                        if (self.board_list[i].column_list[j].hold.color 
                           ==  self.board_list[i - 1].column_list[j - 1].hold.color 
                           == self.board_list[i - 2].column_list[j - 2].hold.color 
                           == self.board_list[i - 3].column_list[j - 3].hold.color):

                            #Switching the winner attribute value to true, indicating that there is a winner in the game
                            self.winner = True
                    
                #Checking if the column position number of the cell is greater than 4, AND if the row position number of the cell is less than or equal to 3
                elif i>3 and j <= 2:

                    #Checking if the cell and 3 cells diagonally up to the right are not empty and each contains the chip
                    if (self.board_list[i].column_list[j].hold
                       and self.board_list[i - 1].column_list[j + 1].hold
                       and self.board_list[i - 2].column_list[j + 2].hold
                       and self.board_list[i - 3].column_list[j + 3].hold):

                        #Checking if the cell and 3 cells diagonally up the the right are matching colors
                        if (self.board_list[i].column_list[j].hold.color 
                           ==  self.board_list[i - 1].column_list[j + 1].hold.color 
                           == self.board_list[i - 2].column_list[j + 2].hold.color 
                           == self.board_list[i - 3].column_list[j + 3].hold.color):

                            #Switching the winner attribute value to true, indicating that there is a winner in the game
                            self.winner = True

                #Checking if the column position number of the cell is greater than 4, AND if the row position number if the cell is greater than 3
                elif i>3 and j>2:

                    #Checking if the cell and 3 cells diagonally up to the left are not empty and each contains the chip
                    if (self.board_list[i].column_list[j].hold
                      and self.board_list[i - 1].column_list[j - 1].hold 
                      and self.board_list[i - 2].column_list[j - 2].hold
                      and self.board_list[i - 3].column_list[j - 3].hold):

                        #Checking if the cell and 3 cells diagonally up to the left are matching colors
                        if (self.board_list[i].column_list[j].hold.color 
                            ==  self.board_list[i - 1].column_list[j - 1].hold.color 
                            == self.board_list[i - 2].column_list[j - 2].hold.color 
                            == self.board_list[i - 3].column_list[j - 3].hold.color):

                            #Switching the winner attribute value to true, indicating that there is a winner in the game
                            self.winner = True
                    
                    
    def is_game_over(self):
        '''Returns the winner boolean variable to check if there is a winner or not.'''

        #Returning the value of the winner which would indicate whether the game is over or not
        return self.winner
            
            
    def get_board(self):
        '''Return the board information'''

        #Returning the board_list attribute to get the board information
        return self.board_list
    

    def is_board_full(self):
        '''Check if the board is full without a winner'''

        #Creating a counter value to count each cell value with the chip in it
        cell_full = 0

        #Checking each column in the board
        for i in range(len(self.board_list)):

            #Checking each cell in the column
            for j in range(len(self.board_list[0].column_list)):

                #Checking if the cell is filled with the chip
                if self.board_list[i].column_list[j].hold != None:

                    #Adds onto the counter value to count how many of the cells are filled
                    cell_full = cell_full + 1

        #Checking if there are 42 filled cells in the board           
        if cell_full == 42:

            #Changing the board_full attribute value to true, indicating that the board is full.
            self.board_full = True

        #Return the value of the attribute board_full in order to show whether the board is full or not
        return self.board_full

    def __repr__(self):

        #Returning printable value
        return self.__str__()


    def __str__(self):
        '''Printable data of the board'''

        #Shows the position number of the columns
        instring='1  2  3  4  5  6  7\n'

        #Creating a small string value to insert in between the value, in order to make it organized
        space = '  '

        #Creating a list in order to store the board information to printable way
        print_list = []

        #Checking each column of the board
        for i in range(len(self.board_list)):

            #Checking each cell of the board
            for j in range(len(self.board_list[i].column_list)):

                #Checking if the cell is not empty
                if self.board_list[i].column_list[j].hold != None:

                    #Replacing the color of the cell to the output_list
                    self.output_list[i][j] = self.board_list[i].column_list[j].hold.color

        #Making position for the number of rows
        for i in range(len(self.output_list[0])):
            
            #Make a list in order to store cells
            print_list.append([])

            #Checking each column number
            for j in range(len(self.output_list)):

                #Add cell to the targeted position
                print_list[i].append(self.output_list[j][i])

        #Checking each list in the list
        for i in print_list:

            #Join the cells in the list together as a string, add it onto the printable value
            instring=instring+(space.join(i))+'\n'

        #Return the printable value   
        return instring
