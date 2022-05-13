from tkinter import * # Import all definitions from tkinter
import tkinter.messagebox
from sudoku_solver import sudoku_solver
import time

X = 'grey60'
Y = 'grey80'
colour = [X, X, X, Y, Y, Y, X, X, X,
          X, X, X, Y, Y, Y, X, X, X,
          X, X, X, Y, Y, Y, X, X, X,
          Y, Y, Y, X, X, X, Y, Y, Y,
          Y, Y, Y, X, X, X, Y, Y, Y,
          Y, Y, Y, X, X, X, Y, Y, Y,
          X, X, X, Y, Y, Y, X, X, X,
          X, X, X, Y, Y, Y, X, X, X,
          X, X, X, Y, Y, Y, X, X, X]

class SudokuSolver:
    # Creates a class instance of the Sudoku Solver GUI
    global colour, L, C, start, end
    
    def __init__(self):
        window = Tk() # Create a window
        window.title("Sudoku Solver") # Set a title
        window.geometry("500x410")
        
        frame = Frame(window) # Create and add a frame to window
        frame.pack()
        
        self.cells = [] # A list of variables tied to entries
        for i in range(9):
            self.cells.append([])
            for j in range(9):
                self.cells[i].append(StringVar())

        index = 0
        for i in range(9):
            for j in range(9):
                Entry(frame, width = 3, justify = 'center', bg=colour[index], font=('Times 25 bold'),
                      textvariable = self.cells[i][j]).grid(row = i, column = j,
                                                            padx = 1, pady = 1)
                index+=1
                
        frame2 = Frame(window) 
        frame2.pack()

        Button(frame2, text = "Solve",
               command = self.solve).grid(row = 2, column = 3)
        Button(frame2, text = "Clear",
               command = self.clear).grid(row = 2, column = 4)

        window.mainloop() # Create an event loop
        
    def solve(self):
        # Solve for the empty spaces in the Sudoku grid and sets
        start = time.time()
        
        values = []
        for i in range(9):
            row = []
            j = 0
            for x in self.cells[i]:
                #Transfers  inputted values in grid to a list
                try:
                    row.append(eval(x.get()))
                    if eval(x.get()) not in range(1,10):
                        error = [i+1,j+1]
                except:
                    if not x.get()=="":
                        row.append(x.get())
                        error = [i+1,j+1]
                    else:
                        row.append(0)
                j+=1
            values.append(row)

        # Calls sudoku solver and gets solution of matrix
        new_answer = sudoku_solver(values)
        
        if new_answer=="Invalid input.":
            tkinter.messagebox.showwarning("Check Sudoku Solution",
                                           f"Invalid input at row: {error[0]}, column: {error[1]} in Sudoku grid.")
        else:
            for i in range(9):
                index = 0
                for x in self.cells[i]:
                    #Sets values in solution to Entry grid
                    x.set(values[i][index])
                    index+=1
                
            end = time.time()
            tkinter.messagebox.showinfo("Solution", f"Solved in {round(end-start,2)} seconds.")
        
    def clear(self):
        # Clears all inputs in the grid when called
        for i in range(9):
            for x in self.cells[i]:
                x.set("")
    
SudokuSolver()
