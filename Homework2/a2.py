#!/usr/bin/python3
# B351/Q351 Fall 2022
# Do not share these assignments or their solutions outside of this class.

import csv
import itertools
from math import fabs

class Board():

    ##########################################
    ####   Constructor
    ##########################################
    def __init__(self, filename):

        # initialize all of the variables
        self.n2 = 0 #length of one side of the board - 9??
        self.n = 0 #length of one side of an inner square
        self.spaces = 0 # total number of cells in sodoku board - 81 cells
        # always change board for adding a new value
        self.board = None # dictionary containing the mapping r,c -> k where k is from 1 to n^2 or 1 to 9, false if k is empty
        # always change these 3 for recording value is now in appropriate row, column, box
        self.valsInRows = None # list that represents mapping of r -> vals where r is row index and vals is set of values currently 1 
        self.valsInCols = None # list mapping of c -> vals where c is the column index and vals is a set of the values in corresponding column
        self.valsInBoxes = None # list that is a mapping of b -> vals wherer b is the inner box index and vals is a set of the values currently ??
        # remove space from unsolved spaces
        self.unsolvedSpaces = None # set of tuples that have unsolved spaces or k = false

        # load the file and initialize the in-memory board with the data
        self.loadSudoku(filename)


    # loads the sudoku board from the given file
    def loadSudoku(self, filename):

        with open(filename) as csvFile:
            self.n = -1
            reader = csv.reader(csvFile)
            for row in reader:

                # Assign the n value and construct the approriately sized dependent data
                if self.n == -1:
                    self.n = int(len(row) ** (1/2))
                    if not self.n ** 2 == len(row):
                        raise Exception('Each row must have n^2 values! (See row 0)')
                    else:
                        self.n2 = len(row)
                        self.spaces = self.n ** 4
                        self.board = {}
                        self.valsInRows = [set() for _ in range(self.n2)]
                        self.valsInCols = [set() for _ in range(self.n2)]
                        self.valsInBoxes = [set() for _ in range(self.n2)]
                        self.unsolvedSpaces = set(itertools.product(range(self.n2), range(self.n2)))

                # check if each row has the correct number of values
                else:
                    if len(row) != self.n2:
                        raise Exception('Each row must have the same number of values. (See row ' + str(reader.line_num - 1) + ')')

                # add each value to the correct place in the board; record that the row, col, and box contains value
                for index, item in enumerate(row):
                    if not item == '':
                        self.board[(reader.line_num-1, index)] = int(item)
                        self.valsInRows[reader.line_num-1].add(int(item))
                        self.valsInCols[index].add(int(item))
                        self.valsInBoxes[self.spaceToBox(reader.line_num-1, index)].add(int(item))
                        self.unsolvedSpaces.remove((reader.line_num-1, index))


    ##########################################
    ####   Utility Functions
    ##########################################

    # converts a given row and column to its inner box number
    def spaceToBox(self, row, col):
        return self.n * (row // self.n) + col // self.n

    # prints out a command line representation of the board
    def print(self):
        for r in range(self.n2):
            # add row divider
            if r % self.n == 0 and not r == 0:
                if self.n2 > 9:
                    print("  " + "----" * self.n2)
                else:
                    print("  " + "---" * self.n2)

            row = ""

            for c in range(self.n2):

                if (r,c) in self.board:
                    val = self.board[(r,c)]
                else:
                    val = None

                # add column divider
                if c % self.n == 0 and not c == 0:
                    row += " | "
                else:
                    row += "  "

                # add value placeholder
                if self.n2 > 9:
                    if val is None: row += "__"
                    else: row += "%2i" % val
                else:
                    if val is None: row += "_"
                    else: row += str(val)
            print(row)


    ##########################################
    ####   Move Functions - YOUR IMPLEMENTATIONS GO HERE
    ##########################################

    # makes a move, records it in its row, col, and box, and removes the space from unsolvedSpaces
    def makeMove(self, space, value):
        spacerow = space[0] #we're looking at this row
        spacecol = space[1] #we're looking at this column
        #ok so space is a (r,c) tuple...
        #1. save the value in board at the appropriate location:
        self.board[space] = value
        #2 record that the value is now in the appropriate row, column, box
        self.valsInRows[spacerow].add(value)
        self.valsInCols[spacecol].add(value)
        self.valsInBoxes[self.spaceToBox(spacerow,spacecol)].add(value)

        #3. remove the space fom unsolved spaces
        self.unsolvedSpaces.remove(space)
        
        #raise NotImplementedError

    # removes the move, its record in its row, col, and box, and adds the space back to unsolvedSpaces
    def undoMove(self, space, value):
        #1. Remove the value from board at the appropriate location
        self.board[space].pop()
        #2. Record that the value is no longer in the appropriate row, column, and box
        self.valsInRows[space[0]].remove(value)
        self.valsInCols[space[1]].remove(value)
        self.valsInBoxes[self.spaceToBox(space)].remove(value)
        #3. Add the space to unsolvedSpaces
        self.unsolvedSpaces.add(space)
        #raise NotImplementedError

    # returns True if the space is empty and on the board,
    # and assigning value to it if not blocked by any constraints (?)
    def isValidMove(self, space, value):
        #returning false if any Sodoku rules are broken
        # 1 - rule: every cell must contain a number between 1 and n
        # i dont think i am implementing that here
        # 2 - rule: there can only be one of each value in a row.
        # 3 - rule: every column must contain only unique values.
        # 4 - rule: Every inner n × n board delineated by bold bordering must contain only unique values.
        # 5 - rule: You must work around the starting values in the board (see below).

        #if its not in the set of unsolved spaces it's full, return false
        if space not in self.unsolvedSpaces:
            return False
        
        spacerow = space[0] #we're looking at this row
        spacecol = space[1] #we're looking at this column
        #checking to see if r and c are within 0 and length of board, else return false
        if spacerow >= self.n2 or spacerow < 0:
            return False
        if spacecol >= self.n2 or spacecol < 0:
            return False
        
        #let's iterate through the row and make sure there isn't already this value
        for item in self.valsInRows[spacerow]:
            if item == value:
                return False
        #let's iterate through the column and make sure there isn't already this value
        for item in self.valsInCols[spacecol]:
            if item == value:
                return False
        #let's iterate through the box and make sure there isn't already this value
        for item in self.valsInBoxes[self.spaceToBox(spacerow,spacecol)]:
            if item == value:
                return False

        #so the space is empty, is a valid row and column for this board, and satisfies constraints:
        return True
        
        #raise NotImplementedError

    # optional helper function for use by getMostConstrainedUnsolvedSpace
    def evaluateSpace(self, space):
        #strategy: number of possibilities should be n2 and then subtract from there
        #so lets start at n2 or 9 for a 9x9 board
        #this is the number of possibilities
        #numberofpossibilities = self.n2
        #this is the set of possibilites (1 to 9)
        setofpossibilities = set(range(1,self.n2+1))

        spacerow = space[0] #we're looking at this row
        spacecol = space[1] #we're looking at this column
        #let's iterate through the row and subtract when we see something already in the row
        for item in self.valsInRows[spacerow]:
            if item in setofpossibilities:
                setofpossibilities.remove(item)
        #let's iterate through the column and subtract from the set when we see a number already in the column
        for item in self.valsInCols[spacecol]:
            if item in setofpossibilities:
                setofpossibilities.remove(item)
        #let's iterate through the box and make sure there isn't already this value
        for item in self.valsInBoxes[self.spaceToBox(spacerow,spacecol)]:
            if item in setofpossibilities:
                setofpossibilities.remove(item)

        #let's count the number of items in the setofpossibilites
        return len(setofpossibilities)


    # gets the unsolved space with the most current constraints
    # returns None if unsolvedSpaces is empty
    def getMostConstrainedUnsolvedSpace(self):
        # if unsolvedspaces is empty.. board is full
        if len(self.unsolvedSpaces) == 0:
            return None
        #else look through unsolved spaces and return unsolved space on the board with the smallest domain of valid value assignments.
        count = 100 #not the right to do it lol
        for rowcol in self.unsolvedSpaces:
            #we want the item with the lowest count
            if self.evaluateSpace(rowcol) < count:
                count = self.evaluateSpace(rowcol)
                #mark that one down in result
                result = rowcol
        
        # return the one with the lowest count
        return result 

class Solver:
    ##########################################
    ####   Constructor
    ##########################################
    def __init__(self):
        pass

    ##########################################
    ####   Solver
    ##########################################

    # recursively selects the most constrained unsolved space and attempts
    # to assign a value to it

    # upon completion, it will leave the board in the solved state (or original
    # state if a solution does not exist)

    # returns True if a solution exists and False if one does not
    def solveBoard(self, board):
        #base case is when unsolved spaces is empty??
        print(len(board.unsolvedSpaces))
        if len(board.unsolvedSpaces) == 0:
            print("done")
            return board

        #inductive step
        else:
            #inductive step
            rowcol = board.getMostConstrainedUnsolvedSpace()
            #iterate through the range 1 to 9
            for num in range(1,board.n2+1):
                #check if it's valid
                if board.isValidMove(rowcol,num):
                    #if it's valid, use assign num to rowcol using makeMove
                    board.makeMove(rowcol,num)
            
                    return self.solveBoard(board)


if __name__ == "__main__":
    # change this to the input file that you'd like to test
    board = Board('tests/example.csv')
    # printing the board first
    board.print()
    print("\n")
    print(board.unsolvedSpaces)



    #now we are solving the board
    s = Solver()
    s.solveBoard(board)


    print("\n\n\n")
    #lets print the new board
    board.print()
    print("\n")
    print(board.unsolvedSpaces)