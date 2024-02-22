import numpy as np
# grids to be used in the in the code
grid = [[5,3,0,0,7,0,0,0,0],               # grid-1.1 :- Right Grid
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

# grid = [[5,3,0,0,7,0,0,0,0],               # grid-1.1 :- Wrong Grid
#         [6,3,0,1,9,5,0,0,0],
#         [0,9,8,0,0,0,0,6,0],
#         [8,0,0,0,6,0,0,0,3],
#         [4,0,0,8,0,3,0,0,1],
#         [7,0,0,0,2,0,0,0,6],
#         [0,6,0,0,0,0,2,8,0],
#         [0,0,0,0,1,9,0,0,5],
#         [0,0,0,0,0,0,0,0,0]]

# grid = [[7,3,0,9,5,0,0,0,0],               # grid-2.1 :- Right Grid
#         [2,0,0,6,7,0,5,8,0],          
#         [0,0,5,0,1,0,4,0,0],
#         [1,9,0,0,6,3,2,0,5],
#         [0,4,0,0,0,0,6,0,0],
#         [5,6,8,2,0,7,0,0,0],
#         [0,2,0,0,8,1,3,0,0],
#         [0,0,1,0,0,9,7,6,0],
#         [0,7,0,5,2,0,8,0,9]] 

# grid = [[7,3,0,9,5,0,0,0,0],               # grid-2.2 :- Wrong Grid
#         [2,0,0,6,7,0,5,8,0],          
#         [0,0,5,0,1,0,4,0,0],
#         [1,9,0,0,6,3,2,0,5],
#         [0,4,0,0,0,0,6,0,0],
#         [5,6,8,2,0,7,0,0,0],
#         [7,2,0,0,8,1,3,0,0],
#         [0,0,1,0,0,9,7,6,0],
#         [0,7,0,5,2,0,8,0,9]] 

# grid = [[0,0,0,9,0,0,0,0,3],               # grid-3
#         [3,4,0,0,1,0,6,0,0],
#         [0,5,6,4,0,0,0,0,8],
#         [1,3,2,6,5,8,0,0,0],
#         [0,9,0,7,4,3,0,6,0],
#         [0,6,4,2,9,1,8,0,0],
#         [0,2,0,0,8,0,3,1,9],
#         [0,0,0,0,2,0,0,8,0],
#         [0,8,0,0,0,9,4,5,0]]

# grid = [[0,0,0,0,0,0,5,0,6],               # grid-4
#         [0,0,5,0,8,0,0,0,4],
#         [0,0,3,2,0,0,1,0,0],
#         [0,0,2,0,7,0,0,0,0],
#         [0,6,4,5,0,0,2,0,0],
#         [0,9,0,1,0,0,0,0,0],
#         [8,7,0,3,0,5,0,0,0],
#         [0,4,0,0,2,6,0,0,5],
#         [0,0,0,0,0,0,4,0,0]]

# grid = [[0,3,5,0,0,0,0,0,6],               # grid-5.1 :- Right Grid
#         [0,0,0,0,7,0,8,0,0],
#         [0,0,1,0,0,9,0,0,0],
#         [9,2,0,0,0,0,0,7,8],
#         [0,5,0,0,0,0,0,2,0],
#         [3,0,0,0,0,0,5,0,0],
#         [0,0,0,5,0,0,0,1,0],
#         [0,9,4,0,0,0,2,0,0],
#         [0,0,0,6,0,7,0,0,4]]

# grid = [[0,3,5,0,3,0,0,0,6],               # grid-5.2 :- Wrong Grid
#         [0,0,0,0,7,0,8,0,0],
#         [0,0,1,0,0,9,0,0,0],
#         [9,2,0,0,0,0,0,7,8],
#         [0,5,0,0,0,0,0,2,0],
#         [3,0,0,0,0,0,5,0,0],
#         [0,0,0,5,0,0,0,1,0],
#         [0,9,4,0,0,0,2,0,0],
#         [0,0,0,6,0,7,0,0,4]]

# this function helps us to present the grid in a more attractive and efficient way.
def print_grid(gr):   
    global grid   # this helps us to use the grid which is outside the function when we are working in the function
    for i in range(len(gr)):                    # we have created a nested for loop to take the rows and columns together             
        if i%3 == 0 and i!=0:                   # this i variable deals with the rows of the grid 
            print("---------------------")
        for j in range(len(gr[0])):             # this j variable deals with the rows of the grid 
            if j%3 == 0 and j!=0:
                print(" | ", end ="")
            if j==8:
                print(gr[i][j])
            else:
                print(str(gr[i][j]) + " ",end="")

# this function checks whether the passed number appears in the following row , column or its small grid(3*3)                 
def possible(row, column, number):
    global grid   # this helps us to use the grid which is outside the function when we are working in the function
    
    #Is the number appearing in the given row?
    for i in range(0,9):                       # this loop runs through the row and then i runs from 0 to 8 from each 
        if grid[row][i] == number:             # row element to another 
            return False

    #Is the number appearing in the given column?
    for i in range(0,9):                       # this loop runs through the column and then i runs from 0 to 8 from each 
        if grid[i][column] == number:          # column element to another 
            return False

    #Is the number appearing in the given square?
    # this piece of code helps us like it knows the starting 
    # position and then it remains in the range of the loops
    # and then it finds whether the number is present in the scope
    # of the loops or not
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3 
    for i in range(0,3):               # every small square/grid has 3 rows             
        for j in range(0,3):           # every small square/grid has 3 columns              
            if grid[y0+i][x0+j] == number:    # if the number is present in that possible 9 combinations then it will return false
                return False  # because that is not our possible solution to our resulting grid
    
    return True  # but if none of the one is the case then it will return true which means
                 # that number is the possible one for the given row column selection
def solve():
    global grid  # this helps us to use the grid which is outside the function when we are working in the function
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:  # here 0 denotes the empty fields and now we check that if there are any empty fields
                for number in range(1,10):   # in the sudoku game the number starts from 1 and ends with 9 
                    if possible(row, column, number):   # we have called the possible function here
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                return
    print(np.matrix(grid))
    print()
    input('MORE POSSIBLE SOLUTIONS TO THE GRID ARE :-')
print("THE ORIGINAL GRID IS :-")    
print()
print_grid(grid)
print()
print("THE SOLUTIONS TO THE ORIGINAL SUDOKU GRID ARE :-")
print()
ng=solve()
print(ng)
print()
