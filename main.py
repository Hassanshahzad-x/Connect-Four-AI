from tkinter import messagebox
from tkinter import *

import random
import pygame
import sys
import math

from Board import Board
from GUI import GUI
from Game import Game

if __name__ == '__main__':
    ROW = 7
    COLUMN = 7
    SQUARE = 100

    board = Board(COLUMN, ROW)
    game = Game()
    gui = GUI(SQUARE, COLUMN * SQUARE, ROW * SQUARE)

    pygame.display.set_caption('CONNECT FOUR')
    pygame.display.update()

    start = gui.start()

    if start:
        gui.draw(board.board, COLUMN, ROW)

    game.turn = random.randint(0, 1)
    game.game_over = False

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.turn == 0:
                    x = event.pos[0]
                    col = int(math.floor(x / SQUARE))

                    if game.valid(board.board, ROW, col):
                        row = game.next(board.board, COLUMN, col)
                        board.board[row][col] = 1

                        gui.draw(board.board, COLUMN, ROW)

                        if game.win(board.board, COLUMN, ROW, 1):
                            Tk().wm_withdraw()
                            messagebox.showwarning('GAME OVER', 'PLAYER 1 WIN!')
                            sys.exit()

                        game.turn += 1
                        game.turn = game.turn % 2

        if game.turn == 1:

            col,score = game.minmax(board.board, 5, -math.inf, math.inf, True, ROW, COLUMN)

            if game.valid(board.board, ROW, col):
                row = game.next(board.board, COLUMN, col)
                board.board[row][col] = 2

                gui.draw(board.board, COLUMN, ROW)

                if game.win(board.board, COLUMN, ROW, 2):
                    Tk().wm_withdraw()
                    messagebox.showwarning('GAME OVER', 'PLAYER 2 WIN!')
                    sys.exit()

                game.turn += 1
                game.turn = game.turn % 2
