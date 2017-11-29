import tkinter as tk
import random
import pygame as pg
from matrix_rotation import rotate_array as ra

class Shape:
    def __init__(self, shape, key, piece, row, column, coords):
        self.shape = shape
        self.key = key
        self.piece = piece
        self.row = row
        self.column = column
        self.coords = coords
class Tetris :
    def __init__(self, parent):
        self.parent = parent
        self.board_width = 10
        self.board_height = 24
        self.board = [[''for column in range(self.board_width)]
                       for row in range(self.board_height)]
        self.width = 300
        self.height = 720
        self.square_width = self.width/10
        self.canvas = tk.Canvas(root, width=self.width, height=self.height)
        self.canvas.grid(row=0, column=0)
        self.separator = self.canvas.create_line(0,
                                                 self.height/6,
                                                 self.width,
                                                 self.height/6,
                                                 width=2)
        self.tickrate = 1000
        self.piece_is_active = False
        self.parent.after(self.tickrate, self.tick)
        self.shapes = {'s':[['*', ''],
                            ['*', '*'],
                            ['', '*']],

                       'z':[['', '*'],
                            ['*', '*'],
                            ['*', '']],

                       'r':[['*', '*'],
                            ['*', ''],
                            ['*', '']],

                       'L':[['*', ''],
                            ['*', ''],
                            ['*', '*']],

                       'o':[['*', '*'],
                            ['*', '*' ]],

                       'I':[['*'],
                            ['*'],
                            ['*'],
                            ['*']],

                       'T':[['*', '*', '*'],
                            ['', '*', '']]
                     }

    def tick(self):
        print('tick')
        if not self.piece_is_active:
            self.spawn()
            self.piece_is_active = True

        self.parent.after(self.tickrate, self.tick)

    def down(self):
        pass

    def lateral(self, direction):
        pass

    def rotate(self, direction):
        pass

    def settle(self):
        pass # this is used to check the height of the board content
        # size is 10 x 20, extra space gives 10 x 24
        self.piece_is_active = not self.piece_is_active

    def spawn(self):
        shape = self.shapes[random.choice('szrLoIT')]
        shape = ra(shape, random.choice((0,90,180,270)))
        width = len(shape[0])
        start = (10-width) //2
        self.active_piece = [shape, [] ]
        for y,row in enumerate(shape):
            self.board[y][start: start+width] = shape[y]
            for x, cell in enumerate(row, start=start):
                if cell:
                    self.active_piece[1].append(
                    self.canvas.create_rectangle(self.square_width*x,
                                                 self.square_width*y,
                                                 self.square_width*(x+1),
                                                 self.square_width*(y+1)))
        for row in self.board:
            print(row)


    def new(self):
        pass

    def lose(self):
        pass

    def clear(self):
        pass

root = tk.Tk()

tetris = Tetris(root)
root.mainloop()