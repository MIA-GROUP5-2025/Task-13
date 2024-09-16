import pygame
import numpy as np

class tictactoe:
    # Draw grid lines
    def __init__(self,screen,linecolor,square_size,height,width,line_width,space,board_rows,board_cols,bg_color,circle_color,cross_color,circle_radius,circle_width,cross_width):
        self.screen = screen
        self.line_color = linecolor
        self.square_size = square_size
        self.width = width
        self.space = space
        self.board_rows = board_rows
        self.board_cols = board_cols
        self.line_width = line_width
        self.circle_color = circle_color
        self.height = height
        self.cross_color = cross_color
        self.board = np.zeros((self.board_rows, self.board_cols))
        self.circle_radius = circle_radius
        self.circle_width = circle_width
        self.cross_width = cross_width
        self.bg_color = bg_color
        self.previous_player = 0
    def draw_lines(self):
        # Horizontal lines
        pygame.draw.line(self.screen, self.line_color, (0, self.square_size), (self.width, self.square_size), self.line_width)
        pygame.draw.line(self.screen, self.line_color, (0, 2 * self.square_size), (self.width, 2 * self.square_size), self.line_width)
        # Vertical lines
        pygame.draw.line(self.screen, self.line_color, (self.square_size, 0), (self.square_size, self.height), self.line_width)
        pygame.draw.line(self.screen, self.line_color, (2 * self.square_size, 0), (2 * self.square_size, self.height), self.line_width)
    
    # Draw figures (circles and crosses)
    def draw_figures(self):
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                if self.board[row][col] == 1:
                    pygame.draw.circle(self.screen, self.circle_color, (int(col * self.square_size + self.square_size // 2), int(row * self.square_size + self.square_size // 2)), self.circle_radius, self.circle_width)
                elif self.board[row][col] == 2:
                    pygame.draw.line(self.screen, self.cross_color, (col * self.square_size + self.space, row * self.square_size + self.square_size - self.space), (col * self.square_size + self.square_size - self.space, row * self.square_size + self.space), self.cross_width)
                    pygame.draw.line(self.screen, self.cross_color, (col * self.square_size + self.space, row * self.square_size + self.space), (col * self.square_size + self.square_size - self.space, row * self.square_size + self.square_size - self.space), self.cross_width)
    
    # Mark a square
    def mark_square(self,row, col, player):
        if self.board[row][col] == 0 and self.previous_player != player:
            self.board[row][col] = player
            self.previous_player = player
    
    # Check if the square is available
    def available_square(self,row, col):
        return self.board[row][col] == 0
    
    # Check if the board is full
    def is_board_full(self):
        return not np.any(self.board == 0)
    
    # Check if there is a winner
    def check_win(self,player):
        # Vertical win
        for col in range(self.board_cols):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                self.draw_vertical_winning_line(col, player)
                return True
    
        # Horizontal win
        for row in range(self.board_rows):
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                self.draw_horizontal_winning_line(row, player)
                return True
    
        # Ascending diagonal win
        if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
            self.draw_asc_diagonal(player)
            return True
    
        # Descending diagonal win
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            self.draw_desc_diagonal(player)
            return True
    
        return False
    
    # Draw vertical winning line
    def draw_vertical_winning_line(self,col, player):
        posX = col * self.square_size + self.square_size // 2
        color = self.circle_color if player == 1 else self.cross_color
        pygame.draw.line(self.screen, color, (posX, 15), (posX, self.height - 15), self.line_width)
    
    # Draw horizontal winning line
    def draw_horizontal_winning_line(self,row, player):
        posY = row * self.square_size + self.square_size // 2
        color = self.circle_color if player == 1 else self.cross_color
        pygame.draw.line(self.screen, color, (15, posY), (self.width - 15, posY), self.line_width)
    
    # Draw ascending diagonal line
    def draw_asc_diagonal(self,player):
        color = self.circle_color if player == 1 else self.cross_color
        pygame.draw.line(self.screen, color, (15, self.height - 15), (self.width - 15, 15), self.line_width)
    
    # Draw descending diagonal line
    def draw_desc_diagonal(self,player):
        color = self.circle_color if player == 1 else self.cross_color
        pygame.draw.line(self.screen, color, (15, 15), (self.width - 15, self.height - 15), self.line_width)
    
    # Restart the game
    def restart(self):
        self.screen.fill(self.bg_color)
        self.draw_lines()
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                self.board[row][col] = 0
