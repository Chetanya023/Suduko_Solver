# Suduko_Solver

This Python project implements a Sudoku solver using a backtracking algorithm. The solver can handle 9x9 Sudoku grids and find a solution by filling in the empty cells based on the rules of the game.

Usage

• Define the Sudoku grid in the code, where 0 represents an empty cell.

• Run the program to find the solution to the Sudoku grid.

• The solver utilizes a backtracking algorithm to systematically fill in the grid, ensuring it adheres to Sudoku rules.

# Define the Sudoku grid (0 represents empty cells)

grid = 

        [[5,3,0,0,7,0,0,0,0],

        [6,0,0,1,9,5,0,0,0],
        
        [0,9,8,0,0,0,0,6,0],
        
        [8,0,0,0,6,0,0,0,3],
        
        [4,0,0,8,0,3,0,0,1],
        
        [7,0,0,0,2,0,0,0,6],
        
        [0,6,0,0,0,0,2,8,0],
        
        [0,0,0,0,1,9,0,0,5],
        
        [0,0,0,0,0,0,0,0,0]]

# Run the solver

solve()

# Output

• The solver prints the original Sudoku grid and its solutions, showcasing its ability to find possible solutions.

Features

• Backtracking algorithm for solving Sudoku puzzles.

• Easy-to-use, with the ability to define and input custom Sudoku grids.

• Provides multiple solutions if applicable.

