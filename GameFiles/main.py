import pygame
import sys
import numpy as np
from TicTacToe import tictactoe
import cv2
from best import detection
# Initialize pygame
pygame.init()

# Constants
WIDTH = 900
HEIGHT = WIDTH
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (13, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Board


# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)
game = tictactoe(screen,LINE_COLOR,SQUARE_SIZE,HEIGHT,WIDTH,LINE_WIDTH,SPACE,BOARD_ROWS,
                 BOARD_COLS,BG_COLOR,CIRCLE_COLOR,CROSS_COLOR,CIRCLE_RADIUS,CIRCLE_WIDTH,CROSS_WIDTH)

model = detection()

# Main loop
game.draw_lines()
player = 1
game_over = False


vc = cv2.VideoCapture(0)

rval = False
while not rval:
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        print("Webcam not connected")
        rval = False

while True:
    rval, frame = vc.read()
    row_scale = HEIGHT/frame.shape[0]
    column_scale = WIDTH/frame.shape[1]
    background_surface = pygame.surfarray.make_surface(np.flipud(np.rot90(frame[:, :, ::-1])))
    background_surface = pygame.transform.scale(background_surface, (WIDTH, HEIGHT))
    screen.blit(background_surface, (0, 0))
    game.draw_figures()

    game.draw_lines()
    if game.check_win(player):
        pass
    else:
        center_x,center_y,class_id = model.detect(rval,frame)
        if center_x:
            # 0:x, 1:0
            #player 1 O, player 2: x
            if class_id == 0:
                player_id = 2
            else:
                player_id = 1
            game.mark_square(int(center_y*row_scale/(HEIGHT/3)),int(center_x*column_scale/(WIDTH/3)),player_id)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if game.available_square(clicked_row, clicked_col):
                game.mark_square(clicked_row, clicked_col, player)
                if game.check_win(player):
                    game_over = True
                else:
                    player = 2 if player == 1 else 1

                game.draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game.restart()
                game_over = False

    pygame.display.update()