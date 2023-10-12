
"""
Alimurat Dinchdonmez, 2031193
420-LCU Computer Programming ,Section 3
Wednesday , April 20
R. Vincent , instructor Assignment 3
"""



'''Simple matrix representation of a Reversi board.

The board is represented as an matrix, or a list of lists, numbered
such that row 0 is the "top" row and column 0 is the leftmost column.

This model is very simple and could be easily adapted to represent any
square (or rectangular) game board, for checkers, chess, etc. It is
meant to illustrate the idea that the representation of the data is
"hidden" from the rest of the game, which only interacts with a
'board' value created by the function board_create()
'''

# If a square contains the value 0 it is empty. Otherwise it contains
# a code defined by the game.

def board_create(rows = 8, cols = 8):
    '''Create a new empty board matrix. 

    The default size is 8x8, as in checkers or chess.'''
    return [[0 for _ in range(cols)] for _ in range(rows)]

def board_rows(board):
    '''Returns the number of rows in the board.'''
    return len(board)

def board_cols(board):
    '''Returns the number of columns in the board.'''
    return len(board[0])

def board_get(board, row, col):
    '''Return the state of a single board position.'''
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        raise ValueError("Illegal row or column.")
    return board[row][col]

def board_put(board, row, col, code):
    '''Place a piece at row, col.'''
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        raise ValueError("Illegal row or column.")
    board[row][col] = code

def board_copy(board):
    '''Construct a copy of the given board.'''
    return [[value for value in row] for row in board]
board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0], [0, 0, 0, 1, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

def board_count(board,value):
    '''Count the number of a value in the board'''
    
    count_val = []
    for i in board:
        for y in i:
            
            if y == value:
                count_val.append(y)
            
            else:
                continue
                
    return len(count_val)  #len is an integer, so the return value is the integer
    
    

# DEFINE THE board_count() FUNCTION HERE!

if __name__ == "__main__":
    print("Testing the board module.")
    # Verify that we can create a board with particular dimensions.
    b = board_create(5, 4)
    assert board_rows(b) == 5
    assert board_cols(b) == 4
    b = board_create()
    assert board_rows(b) == 8
    assert board_cols(b) == 8
    # Check operation of get() and count()
    assert board_get(b, 0, 0) == 0
    try:
        board_get(b, -1, -1)
    except ValueError:
        pass
    else:
        assert False # Failed to raise ValueError
        
    try:
        board_get(b, board_rows(b), board_cols(b))
    except ValueError:
        pass
    else:
        assert False # Failed to raise ValueError
    assert board_count(b, 1) == 0
    # Place a first value and verify it works.
    board_put(b, 0, 0, 1)
    assert board_get(b, 0, 0) == 1
    assert board_count(b, 1) == 1
    # Place and verify a second value.
    board_put(b, 1, 1, 1)
    assert board_get(b, 1, 1) == 1
    assert board_get(b, 0, 1) == 0
    assert board_count(b, 1) == 2
    assert board_count(b, 0) == board_rows(b) * board_cols(b) - 2
    # Make a copy of the board.
    c = board_copy(b)
    assert b is not c
    assert b[0] is not c[0]
    assert board_count(c, 1) == 2
    assert board_count(c, 0) == board_rows(c) * board_cols(c) - 2
    # Place an additional value in board 'b', make sure it does
    # not appear in 'c'
    board_put(b, 2, 2, 1)
    assert board_count(b, 1) == 3
    assert board_count(c, 1) == 2
    assert board_get(c, 2, 2) == 0
    print("All tests passed.")
