import numpy as np

def check_row(row, char):
    #Returns True if char not in row
    if char in row:
        return False
    else:
        return True

def check_column(matrix, char, pos):
    #Returns True if char not in column
    to_check = []
    col = pos[1]
    for i in range(len(matrix)):
        to_check.append(matrix[i][col])

    if char in to_check:
        return False
    else:
        return True

def check_box(matrix, char, pos):
    #Returns True if char not in sectioned box
    to_check = []
    row, col = pos[0], pos[1]
    start_row, start_col = (row//3)*3, (col//3)*3
    
    for i in range(3):
        for j in range(3):
            to_check.append(matrix[start_row+i][start_col+j])
            
    if char in to_check:
        return False
    else:
        return True

def checker(row, matrix, char, pos):
    boolean = check_row(row, char) and check_column(matrix, char, pos) and check_box(matrix, char, pos)
    return boolean
          
def sudoku_solver(array):
    """
    Function 'sudoku_solver' takes in a 9×9 array of numbers representing a Sudoku grid and returns a new grid with solution.
    """
    options = range(1,10)
    to_check = []
    
    #Handling errors with input
    if isinstance(array,list) and len(array)==9:
        for list_ in array:
            if isinstance(list_,list) and len(list_)==9:
                for char in list_:
                    if char==0 or (char in options):
                        pass
                    else:
                        return "Invalid input."
            else:
                return "Invalid input."
    else:
        return "Invalid input."

    #Gets all empty spaces in grid to be filled
    for row in range(9):
        for col in range(9):
            if array[row][col]==0:
                to_check.append([row,col])
    i = 0
    while i!=len(to_check):
        try:
            current_row = array[to_check[i][0]]
                 
            r,c = to_check[i]
            current_char = array[r][c]
            next_ = 0

            #Gets possible solution to empty space
            try_ = options[current_char+next_]
            #Checks if it satisfies its position and sets it
            while not checker(current_row, array, try_, to_check[i]):
                next_+=1
                try_ = options[current_char+next_]
                    
            else:
                array[r][c]=try_
                i+=1
        except:
            #If no possible solution was found, backtracks to find new solutions
            array[r][c]=0
            i-=1
        
    return np.matrix(array)
