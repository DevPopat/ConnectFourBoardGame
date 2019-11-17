
#Creating a GUI for the boardgame

#importing all modules necessary for functionality 

import pygame
from pygame.locals import *
import sys
class View():

    def __init__(self):
        
        """Creating the game window"""
        
        #initializing pygame 
        pygame.init()
        
        #setting the screen size to 512 x 512 and initializing the display
        self.screen_size = (512, 512)
        self.screen = pygame.display.set_mode(self.screen_size)
        
        #setting the horizontal and vertical difference between each cell in the connect four board 
        self.horiz_diff = int(self.screen_size[0] // 7)
        self.vert_diff = self.screen_size[1] // 6
        
        #setting the window's caption to be 'Connect Four'
        pygame.display.set_caption('Connect Four')
        
        # We want to place the cells in the middle of the horizontal difference. Thus we define horiz_space and vert_space accordingly.
        self.cel_horiz_pos = int(self.horiz_diff // 2)
        self.cel_vert_pos = int(self.vert_diff // 2)
        
        #Creating a Surface object and storing it in the variable self.background. Filling the surface with the appropriate shade of blue.
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((60, 180, 200))
        
        #setting the default click position to 0.
        self.last_click_pos = 0
        
        #A boolean quit game variable set to false initially.
        self.quit = False

    def mock_board(self):
        """Creating an empty board when the game begins."""
        
        #loop that will create the 6x7 empty connect four board 
        for i in range(7):
            for j in range(6):
                #drawing a circle on the correct spot 
                pygame.draw.circle(self.background, (250,250,250), [self.cel_horiz_pos, self.cel_vert_pos], 20)
                
                #updating the vertical location for the next cell 
                self.cel_vert_pos = self.cel_vert_pos + self.vert_diff
                
            #Resetting self.cel_vert_pos back to its original value for the next row
            self.cel_vert_pos = int(self.vert_diff // 2)
            # Incrementing the horiz_space by horiz_diff
            self.cel_horiz_pos = self.cel_horiz_pos + self.horiz_diff
            
        #Drawing the changes over the surface
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
            
    def get_column_number(self, board):
        
        """A method that gets the number of the column that the player clicked on"""
        
        #setting an infinite loop
        while True:
            
            #assigning the horizontal coordinate ranges of each column number
            col_1 = range(1, self.horiz_diff)
            col_2 = range(self.horiz_diff, 2 * self.horiz_diff)
            col_3 = range(2 * self.horiz_diff, 3 * self.horiz_diff)
            col_4 = range(3 * self.horiz_diff, 4 * self.horiz_diff)
            col_5 = range(4 * self.horiz_diff, 5 * self.horiz_diff)
            col_6 = range(5 * self.horiz_diff, 6 * self.horiz_diff)
            col_7 = range(6 * self.horiz_diff, 7 * self.horiz_diff)
            
            #if the player clicks the 'x' button, the program shuts down 
            for event in pygame.event.get():   
                if event.type == QUIT:
                    # Change self.quit to True when the 'x' button is clicked
                    self.quit = True
                    sys.exit()                 
            
                #If the game is over, we do not want the players to make more moves, therefore pass.
                elif board.is_game_over() == True or board.is_board_full() == True:
                    pass
                
                #if the mouse is pressed 
                elif pygame.mouse.get_pressed()[0] == True:
                    
                    # if this is a duplicate click, ignore it
                    if self.last_click_pos == pygame.mouse.get_pos():
                        return 
                    
                    #if it isn't a duplicate click save the last position where it was clicked in a tuple
                    else:
                        self.last_click_pos = pygame.mouse.get_pos()
                    
                    
                    #save the last clicked position as last_click_pos 
                    last_click_pos = self.last_click_pos
                    
                    #depending on the horizontal coordinate of the last click position, the number of the column is returned 
                    if last_click_pos[0] in col_1:    
                        return 0
                    elif last_click_pos[0] in col_2:
                        return 1
                        
                    elif last_click_pos[0] in col_3:
                        return 2
                        
                    elif last_click_pos[0] in col_4:
                        return 3
                        
                    elif last_click_pos[0] in col_5:
                        return 4
                        
                    elif last_click_pos[0] in col_6:
                        return 5
                        
                    elif last_click_pos[0] in col_7:
                        return 6 
                    
                else:
                    
                    #if the mouse is not clicked, None is returned 
                    return None 
    
    def draw_board(self, board):
        """A method drawing the pygame board with the appropriate changes made to the connect four board."""
        
        #gets the horizontal and vertical position of each cell. We want to place the cell in the middle of the horiz_diff and vert_diff.
        game_cell_horiz_pos = int(self.horiz_diff // 2)
        game_cell_vert_pos = int(self.vert_diff // 2)
        
        #Looping through the board_list of the connect four board object.              
        for i in range(len(board.board_list)):
            
            for j in range(len(board.board_list[i].column_list)):
                
                # a loop that checks the connect four board to see the color in a specific cell and then changes the pygame cell to be the same color
                
                # Checks to see if the current turn is of player 'R' and checks if the current cell in the board_list contains a 'Y' chip
                if board.board_list[i].column_list[j].hold != None and board.board_list[i].column_list[j].hold.color != 'Y' and board.chip_color == 'R':
                    
                    # Draw a red circle
                    pygame.draw.circle(self.background, (255,0,0), [game_cell_horiz_pos, game_cell_vert_pos], 20)
                    
                    # Increment the game_cell_vert_pos by self.vert_diff
                    game_cell_vert_pos = game_cell_vert_pos + self.vert_diff
                   
                # Checks if the current cell in board_list holds a Red chip and if the current turn is of player 'Y'
                elif board.board_list[i].column_list[j].hold != None and board.board_list[i].column_list[j].hold.color != 'R' and board.chip_color == 'Y':
                    
                    # Draw a yellow circle
                    pygame.draw.circle(self.background, (255,255,0), [game_cell_horiz_pos, game_cell_vert_pos], 20)
                    
                    # Increment the game_cell_vert_pos by self.vert_diff
                    game_cell_vert_pos = game_cell_vert_pos + self.vert_diff
                   
                else:
                    
                        # Checks if the current cell in board_list holds a Red chip. We want to keep the red chip in that position and not overdraw on it.                    
                    if board.board_list[i].column_list[j].hold != None and board.board_list[i].column_list[j].hold.color == 'R':
                        
                        # Redraw red circle in that position
                        pygame.draw.circle(self.background, (255,0,0), [game_cell_horiz_pos, game_cell_vert_pos], 20)
                       
                        # Increment the game_cell_vert_pos by self.vert_diff
                        game_cell_vert_pos = game_cell_vert_pos + self.vert_diff
                        
                        # Checks if the current cell in board_list holds a Yellow chip. We want to keep the yellow chip in that position and not overdraw on it.                    
                    elif board.board_list[i].column_list[j].hold != None and board.board_list[i].column_list[j].hold.color == 'Y':
                       
                        # Redraw yellow circle in that position
                        pygame.draw.circle(self.background, (255,255,0), [game_cell_horiz_pos, game_cell_vert_pos], 20)
                       
                        # Increment the game_cell_vert_pos by self.vert_diff
                        game_cell_vert_pos = game_cell_vert_pos + self.vert_diff
                        
                    #Checks to see if the cell is empty and keeps the cell color black     
                    elif board.board_list[i].column_list[j].hold == None:
                        
                        # Redraw a black circle in that position
                        pygame.draw.circle(self.background, (250,250,250), [game_cell_horiz_pos, game_cell_vert_pos], 20)
                        
                        # Increment the game_cell_vert_pos by self.vert_diff
                        game_cell_vert_pos = game_cell_vert_pos + self.vert_diff
            
            # Reset the game_cell_vert_pos for the next row
            game_cell_vert_pos = int(self.vert_diff // 2)
            
            # Increment game_cell_horiz_pos by self.horiz_diff
            game_cell_horiz_pos = game_cell_horiz_pos + self.horiz_diff
            
        #blitting/redrawing all the changes to the board     
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
    
    def winner_message_red(self):
        """A method that creates a message declaring red to be the winner"""
        
        #create a Font object and setting the font size
        sys_font = pygame.font.SysFont(None, 60)
        
        #creating the message and setting the font color to red  
        rendered = sys_font.render('Red Wins!',0,(225,0,0))
        
        #blitting/redrawing all the changes made to the background
        self.screen.blit(rendered,(150,150))            
        
        #updating the changes made
        pygame.display.update()
        
    def winner_message_yellow(self):
        """A method that creates a message declaring red to be the winner"""

        #create a Font object and setting the font size
        sys_font = pygame.font.SysFont(None, 60)
        
        #creating the message and setting the font color to yellow  
        rendered = sys_font.render('Yellow Wins!',0,(225,255,0))
        
        #blitting/redrawing all the changes made to the background
        self.screen.blit(rendered,(150,150))
        
        #updating the changes made
        pygame.display.update()
    
    def tie_message(self):
        """A method that creates a message declaring a tie"""
        
        #create a Font object and setting the font size
        sys_font = pygame.font.SysFont(None, 60)
        
        #creating the message and setting the font color to white  
        rendered = sys_font.render('It is a tie!',0,(255,255,255))
        
        #blitting/redrawing all the changes made to the background 
        self.screen.blit(rendered,(150,150))
        
        #updating the changes made
        pygame.display.update()
