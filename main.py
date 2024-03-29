from SudokuBoard import SudokuBoard
from SudokuSolver import SudokuSolver
import time


completeboard = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],

    [3, 1, 2, 6, 4, 5, 9, 7, 8],
    [9, 7, 8, 3, 1, 2, 6, 4, 5],
    [6, 4, 5, 9, 7, 8, 3, 1, 2],

    [2, 3, 1, 5, 6, 4, 8, 9, 7],
    [8, 9, 7, 2, 3, 1, 5, 6, 4],
    [5, 6, 4, 8, 9, 7, 2, 3, 1]
]

easy = [
    [7, 0, 0, 0, 0, 0, 0, 6, 3],
    [0, 0, 2, 6, 7, 3, 4, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],

    [0, 3, 9, 0, 0, 0, 2, 0, 1],
    [5, 7, 4, 0, 2, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 5, 8, 7, 0],

    [1, 8, 0, 2, 6, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 7, 0, 2, 8],
    [0, 6, 0, 0, 9, 0, 1, 0, 0]
]

medium = [
    [0, 0, 9, 8, 0, 0, 0, 0, 7],
    [2, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 5, 0, 6],

    [9, 0, 2, 1, 8, 0, 4, 0, 0],
    [6, 5, 0, 0, 0, 0, 0, 1, 8],
    [0, 0, 8, 0, 4, 2, 7, 0, 9],

    [5, 0, 1, 0, 9, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 2],
    [4, 0, 0, 0, 0, 7, 1, 0, 0]
]

hard = [
    [0, 5, 7, 0, 1, 4, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 7, 9, 0, 0],

    [0, 3, 0, 0, 9, 0, 0, 0, 1],
    [0, 0, 6, 4, 5, 8, 7, 0, 0],
    [7, 0, 0, 0, 3, 0, 0, 9, 0],

    [0, 0, 4, 8, 0, 0, 0, 0, 0],
    [0, 0, 9, 0, 0, 0, 0, 0, 8],
    [0, 0, 0, 2, 4, 0, 5, 3, 0]
]

hard2 = [
    [7, 0, 0, 9, 0, 0, 6, 0, 8],
    [0, 0, 9, 8, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 7, 0, 0, 9, 0],

    [9, 0, 0, 5, 0, 0, 0, 0, 2],
    [0, 6, 0, 0, 2, 0, 0, 5, 0],
    [4, 0, 0, 0, 0, 7, 0, 0, 9],

    [0, 7, 0, 0, 8, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 2, 3, 0, 0],
    [6, 0, 8, 0, 0, 5, 0, 0, 1]
]

easy_board = SudokuBoard(easy)
easy_solver = SudokuSolver(easy_board)
medium_board = SudokuBoard(medium)
medium_solver = SudokuSolver(medium_board)
# able to solve with row/column elimination^

hard_board = SudokuBoard(hard)
hard_solver = SudokuSolver(hard_board)
# unable to solve with row/column elimination^

start_time_ms = time.time()  * 1000
medium_solver.solve_board()
end_time_ms = time.time() * 1000
print(f"elapsed time(ms):{end_time_ms - start_time_ms}")