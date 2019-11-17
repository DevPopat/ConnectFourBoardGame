""" Dev Popat  Meryl Marasigan 
    74688458   16565488
    popatd     mpmarasi
"""

#mporting all the necessary modules for functionality 
from hw7_view import View
from connect_four_board import Board

#creating board and view objects 
board = Board()
view = View()

#creating the blank board 
view.mock_board()

# While game not over (there is no winner and there is no tie yet)
while view.quit == False:

    # get column number for the next move
    column_number = view.get_column_number(board)
    
    # If there is a move from the user
    if column_number != None:
        
        # attempt to make the move
        was_move_legal = board.make_move(column_number)
        
        
        # if the move is legal,
        if was_move_legal == None:
            
            # the move has been made, so update the board
            view.draw_board(board)
            
            print(board.chip_color)
            print(board.__str__())
            
            #Change turn
            board.whose_turn()
        
            #Check for winner(horizontally, vertically, or diagonally)
            board.vertical_win()
            board.horizontal_win()
            board.diagonal_win()
            #was_move_legal = board.make_move(column_number)

    #if the game is over (meaning there is a winner or it is a tie), 
    if board.is_game_over() == True:
        
        #checking the current chip color 
        
        #if the chip color is red (meaning it's currently the red player's turn)
        if board.chip_color == 'R':
            
            #yellow is declared as the winner  (because after the winning move is made, the players still switch) via a message 
            view.winner_message_yellow()
            
        #if the current chip color is yellow, (meaning it's currently the red player's turn)
        elif board.chip_color == 'Y':
            
            #red is declared as the winner (because after the winning move is made, the players still switch) via a message 
            view.winner_message_red()
            
        #if there no winner, display a tie message 
        else:
            view.tie_message()             
