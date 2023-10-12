

"""
Alimurat Dinchdonmez, 2031193
420-LCU Computer Programming ,Section 3
Wednesday , April 20
R. Vincent , instructor Assignment 3
"""

'''User interface code for Reversi

Includes the main program, so this is the file to run to play a game.

This code uses a number of features of Python and tkinter that go
beyond the scope of the course material covered so far. You are
welcome to read this file and ask questions about it, but for this
assignment, you are not responsible for knowing the programming
techniques used here.
'''

import tkinter as tk
from tkinter import messagebox
from board import *
from game import *

def left_mouse_down(event):
    '''Handle a mouse button press.'''
    # Scale mouse coordinates down to a board row and column.
    row = event.y // PIXELS_PER_SQUARE
    col = event.x // PIXELS_PER_SQUARE
    if game_turn(board, row, col):
        draw_board(board)
        if game_over(board):
            winner = game_winner(board)
            if winner == 0:
                message = "Tie game"
            else:
                message = "Player {} wins!".format(winner)
            messagebox.showinfo('Game over', message)
            root.destroy()

def draw_board(board):
    '''Draw the Reversi board.

    Removes all of the existing pieces, and then redraws the new configuration.
    '''
    piece_colors = {HUMAN: 'black', COMPUTER: 'white' }
    
    # Delete pieces
    for item in canvas.find_withtag('piece'):
        canvas.delete(item)

    # Insert new pieces at the appropriate coordinates
    for row in range(board_rows(board)):
        for col in range(board_cols(board)):
            player = board_get(board, row, col)
            if player != 0:
                # Scale row and column into pixel coordinates.
                y = row * PIXELS_PER_SQUARE
                x = col * PIXELS_PER_SQUARE
                canvas.create_oval(x + 2, y + 2,
                                   x + PIXELS_PER_SQUARE - 2,
                                   y + PIXELS_PER_SQUARE - 2,
                                   fill = piece_colors[player],
                                   tag = 'piece')
        
board = game_start()            # Create the initial board.
PIXELS_PER_SQUARE = 50          # Pixels per square
BOARD_PIXELS = PIXELS_PER_SQUARE * board_rows(board)
MEDIUM_GREEN = "#005400"        # About 1/3 green intensity.

# Initialize tkinter and create the basic window structure.

root = tk.Tk()
root.title('Reversi')

# Create the square canvas object where all game activity is drawn. It has
# a black background onto which I'll draw the green squares.

canvas = tk.Canvas(root, width = BOARD_PIXELS, height = BOARD_PIXELS,
                   bg = 'black')
canvas.pack()

# Tell tkinter that left mouse button clicks will be processed by the
# 'left_mouse_down' function defined above.

canvas.bind('<Button-1>', left_mouse_down)

# Draw the 64 board squares in medium green.

for row in range(board_rows(board)):
    for col in range(board_cols(board)):
        # Scale up row and column to pixel coordinates.
        x = col * PIXELS_PER_SQUARE
        y = row * PIXELS_PER_SQUARE
        # Create rectangle, leaving a small black border around it.
        canvas.create_rectangle(x + 1, y + 1,
                                x + PIXELS_PER_SQUARE - 1,
                                y + PIXELS_PER_SQUARE - 1,
                                fill = MEDIUM_GREEN)

draw_board(board)
root.mainloop()                 # Run the 'main loop' of tkinter.
