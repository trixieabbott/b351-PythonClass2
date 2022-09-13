import csv
import itertools
from math import fabs

class Board():

    ##########################################
    ####   Constructor
    ##########################################
    def __init__(self, filename):

        # initialize all of the variables
        self.n2 = 0 #length of one side of the board
        self.n = 0 #length of one side of an inner square
        self.spaces = 0 # total number of cells in sodoku board - 81 cells
        # always change board for adding a new value
        self.board = None # dictionary containing the mapping r,c -> k where k is from 1 to n^2 or 1 to 9, false if k is empty
        # always change these 3 for recording value is now in appropriate row, column, box
        self.valsInRows = None # list that represents mapping of r -> vals where r is row index and vals is set of values currently 1 
        self.valsInCols = None # list mapping of c -> vals where c is the column index and vals is a set of the values in corresponding column
        self.valsInBoxes = None # list that is a mapping of b -> vals wherer b is the inner box index and vals is a set of the values currently
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

    ##move functions

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

    # gets a list of unsolved spaces sorted by most constraints to least constraints
    # returns None if unsolvedSpaces is empty
    def getMostConstrainedUnsolvedSpace(self):
        # if unsolvedspaces is empty.. board is full
        listofconstraints = []

        if len(self.unsolvedSpaces) == 0:
            return None
        #else look through unsolved spaces and return unsolved space on the board with the smallest domain of valid value assignments.
        for rowcol in self.unsolvedSpaces:
            listofconstraints.append((rowcol,int(self.evaluateSpace(rowcol))))
        
        # return a list of tuples of unsolved space of (space, number of constraints) sorted by least to most constraints
        return sorted(listofconstraints, key=lambda x: x[1])


if __name__ == "__main__":
    # change this to the input file that you'd like to test
    board = Board('tests/test-2-medium/15.csv')
    # printing the board first
    print("\nBOARD BEFORE\n")
    board.print()
    print("\nthis is the number of unsolved spaces left:")
    print(len(board.unsolvedSpaces))

    print(board.getMostConstrainedUnsolvedSpace())


    #questions - my solver only works on easy, because it only goes once over
    # how do i keep track of the starting values in the board?