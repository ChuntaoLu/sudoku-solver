import random
# Sudoku solver with heuristic
#
# A Sudoku board is a 9-by-9 grid of squares. There are totally 27 units on
# the grid: 9 rows, 9 columns and 9 3-by-3 boxes. Solving a Sudoku is to fill
# the squares with numbers range from 1 to 9 so that none of the 27 units have
# duplicates.


#===============================
# Data definitions:
# Board is a list of 81 elements, each range from 1 to 9.

# Constants:
ROWS = [[i * 9 + j for j in range(9)] for i in range(9)]
COLS = [[i + j * 9 for j in range(9)] for i in range(9)]
BOXES = [[(i // 3) * 18 + i * 3 + (j // 3) * 9 + j % 3 for j in range(9)]
         for i in range(9)]
UNIT_TABLE = {(i * 9 + j): set(ROWS[i] + COLS[j] + BOXES[(i // 3) * 3 + (j // 3)])
              for i in range(9) for j in range(9)}


#===============================
# Functions:
def solve(board):
    """
    Board -> Board
    produce a solution to a given board, false if unsolvable.

    Steps:
    1. Check if board is already solved, if so return board, else step 2;
    2. Fill the blank square which has least valid number choices to generate a
       list of new boards, which are closer to a solution;
    3. Repeat step 1 and 2 until a solution is found or return False if all
       squares are filled and yet no solution found(unsolvable).
    """

    if is_solved(board):
        return board
    else:
        for new_board in fill_board(board):
            a_try = solve(new_board)
            if a_try:
                return a_try
        return False
    ###########DFS approach#############
    ##board_stack adds overhead, slower than tail recursion above
    #board_stack = [board]
    #while board_stack:
    #    current_board = board_stack.pop()
    #    if is_solved(current_board):
    #        return current_board
    #    else:
    #        board_stack += next_boards(current_board)
    #return False


def is_solved(board):
    """
    Board -> Boolean
    produce true if given board is solved
    """
    return False not in board


def fill_board(board):
    """
    Board -> (listof Board)
    produce a list of new boards by filling in the blank square of least choices.

    With least choices of numbers to fill in the blank square, we maximize the
    possibility to fill in a right number, hence this is a good heuristic.

    By randomly traversing the blank squares, we could have a better chance to
    find a square of only choice early, and on average get better performance.
    """
    least_choices = range(1, 10)
    blank_square_indices = [i for i in range(81) if not board[i]]
    random.shuffle(blank_square_indices)
    for square_index in blank_square_indices:
        choices = valid_fills(board, square_index)
        if len(choices) < len(least_choices):
            least_choices = choices
            least_index = square_index
            if len(least_choices) == 1:
                break
    board_list = []
    for num in least_choices:
        new_board = board[:]
        new_board[least_index] = num
        board_list.append(new_board)
    return board_list


def valid_fills(board, square_index):
    """
    Board index -> (setof Number)
    produce a set of all valid numbers to fill a given board at given square index.
    """
    return set(range(1, 10)) - set([board[i] for i in UNIT_TABLE[square_index]])
