import numpy


class Board:
    def __init__(self, row, column):
        self.board = numpy.zeros((row, column))

    def print(self,board):
        print(numpy.flip(board, 0))
