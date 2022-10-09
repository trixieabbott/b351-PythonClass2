#!/usr/bin/python3

# B351/Q351 Fall 2022
# Do not share these assignments or their solutions outside of this class.

###################################
#                                 #
# Assignment 3: Search Algorithms #
#                                 #
###################################

from curses import curs_set
from typing import final
import State
import Board
import heapq

STOP = -1
CONTINUE = 0



#################################
# Problem 1 - Fringe Expansion
#################################
# Objective:
# 1) Write a function that adds the possible states that we can get to
#    from the current state to the end of the fringe.
#
# Notes:
# (1) This function should not return or yield anything but just update the contents of the fringe
# (2) board_object.slide_blank is error-safe. It will return None if it is impossible to slide the blank

def expand_fringe(current_state, fringe):
    #so current state is a state made up of simple_board, no parent state, 0 depth, 0 fvalue
    #let's grab the board
    theboard = current_state.board

    #here are the moves we want to iterate through
    moveOne = (0,1)
    moveTwo = (0,-1)
    moveThree = (-1,0)
    moveFour = (1,0)
    list = [moveOne,moveTwo,moveThree,moveFour]
    #seeing if these moves will work on theboard
    for move in list:
        if theboard.slide_blank(move):
            fringe.append(State.State(theboard.slide_blank(move), current_state, 0, current_state.depth+1))


########################################
# Problem 2 - BFS (Breadth First Search)
########################################
# Objectives:
# (1) Write a function that implements a single iteration of the BFS algorithm
#     by considering the first state from the fringe.
#     (Returns STOP if the fringe is empty.)
#     See the project documentation for more details.

def breadth_first_search(fringe, max_depth, goal_board):
    #fringe is made up of a list of states(board,parent state,depth,fvalue)

    #stops when the fringe is emtpy
    if fringe == []:
        return STOP
    else:
        #pops the first state in the fringe
        currstate = fringe.pop(0)
        #checks if goal board
        if (currstate.board == goal_board):
            return currstate
        #ignores states deepr than max depth
        elif (currstate.depth > max_depth):
            return CONTINUE
        #expands the fringe
        else:
            expand_fringe(currstate,fringe)
            return CONTINUE
        



def uninformed_solver(start_board, max_depth, goal_board):
    """
        Looping function which calls breadth_first_search until it finds a solution (a State object) or
        until STOP has been returned. Does not consider States below max_depth.
        If the goal is reached, this function should return the Goal State,
        which includes a path to the goal. Otherwise, returns None.
    """
    fringe = [State.State(start_board, None, 0, 0)]
    found = CONTINUE
    while found == CONTINUE:
        found = breadth_first_search(fringe, max_depth, goal_board)
    if isinstance(found, State.State):
        # Found goal!
        return found
    # Max depth reached...
    return None


####################################
# Problem 3 - UCS f-value Function
####################################
# Objectives:
# (1) Write a function that takes a board and depth and returns the f-value
#     (priority) that board should have in a uniform-cost search scenario.

def ucs_f_function(board, current_depth):
    return current_depth


###########################################
# Problem 4 - A* f-value Function Factory
###########################################
# Objectives:
# (1) Given a heuristic function and a goal board, returns a f-value FUNCTION
#     (like ucs_f_function) that evaluates boards and depths as in the A* algorithm.
#
# Notes:
# (1) It may be helpful to consult your solution for a1.compose here.

def a_star_f_function_factory(heuristic, goal_board):
    #heuristic is a function
    #returns a function where you pass the current board 
    #composed function = lambda x: f_outer(f_inner(x))
    theFunctiion = lambda board, current_depth: current_depth + heuristic(board, goal_board)
    return theFunctiion


# Here is an example heuristic function.
def manhattan_distance(current_board, goal_board):
    total = 0
    goal_matrix = goal_board.matrix
    for goal_r in range(len(goal_board.matrix)):
        for goal_c in range(len(goal_board.matrix[0])):
            val = goal_matrix[goal_r][goal_c]
            if val == 0:
                continue
            current_r, current_c = current_board.find_element(val)
            total += abs(goal_r - current_r) + abs(goal_c - current_c)
    return total

#################################
# Problem 5 - Your Own Heuristic
#################################
# Objectives:
# (1) Write a function that takes current_board and goal_board as arguments and
#     returns an estimate of how many moves it will take to reach the goal board.
#     Your heuristic must be admissible (never overestimate cost to goal), but
#     it does not have to be consistent (never overestimate step costs).
#
# Notes:
# (1) This heuristic should be admissible, but greater than (closer to the real
#     value than) the manhattan distance heuristic on average. That makes it a
#     better heuristic.


def my_heuristic(current_board, goal_board):
    sum = 0

    for i in range(0,3):
        for j in range(0,3):
            if current_board.matrix[i][j] != goal_board.matrix[i][j]:
                sum += 1
    
    return sum - 1

#################################
# Problem 6 - Informed Expansion
#################################
# Objectives:
# (1) Write a function that expands the fringe using the f-value function
#     provided. Note that States automatically sort by their f-values.
#
# Notes:
# (1) This function should update the contents of the fringe using heapq.


def informed_expansion(current_state, fringe, f_function):
    heapq.heapify(fringe)
    
    theboard = current_state.board
    
    #here are the moves we want to iterate through
    moveOne = (0,1)
    moveTwo = (0,-1)
    moveThree = (-1,0)
    moveFour = (1,0)
    list = [moveOne,moveTwo,moveThree,moveFour]
    #seeing if these moves will work on theboard
    for move in list:
        if theboard.slide_blank(move):
            heapq.heappush(fringe,State.State(theboard.slide_blank(move), current_state, 0, f_function))


#################################
# Problem 7 - Informed Search
#################################
# Objectives:
# (1) Write a function that implements a single iteration of the
#     A*/UCS algorithm by considering the top-priority state from the fringe.
#     (Returns STOP if the fringe is empty.)
#     See the project documentation for more details.


def informed_search(fringe, goal_board, f_function, explored):
    #step 1
    if fringe == []:
        return STOP
    else:
        #step 2 uses heapop ot get the highest priority state from the fringe
        currstate = heapq.heappop(fringe)
        #step 5 returns goal sttate when found
        if (currstate.board == goal_board):
            return currstate

        #not sure how to use this
        theFunction = a_star_f_function_factory(f_function,goal_board)

        #step 3:
        if (theFunction(currstate)>=explored[currstate]):#is not smaller than previous f value):
            return CONTINUE

        #step 4
        explored[currstate.board].append(theFunction(currstate))
        #step 6
        
        informed_expansion(currstate,fringe,theFunction)
        return CONTINUE


def informed_solver(start_board, goal_board, f_function):
    """
        Looping function which calls informed_search until it finds a solution
        (a State object) or until STOP has been returned.
        If the goal is reached, this function should return the Goal State,
        which includes a path to the goal. Otherwise, returns None.
    """
    fringe = [State.State(start_board, None, 0, f_function(start_board, 0))]
    explored = {}
    found = CONTINUE
    while found == CONTINUE:
        found = informed_search(fringe, goal_board, f_function, explored)
    if isinstance(found, State.State):
        return found
    return None


def ucs_solver(start_board, goal_board):
    return informed_solver(start_board, goal_board, ucs_f_function)


def a_star_solver(start_board, goal_board, heuristic):
    f_function = a_star_f_function_factory(heuristic, goal_board)
    return informed_solver(start_board, goal_board, f_function)

#################################
# Bonus Problem - IDS (10pts)
#################################
# Implement IDS in any way you choose. You will probably want to write multiple
# helper functions; be sure to document these appropriately.
#
# ids should take a start board and goal board and then perform multiple
# depth-first searches, with the maximum depth increasing from 0 all the way to
# final depth.
#
# If there is a solution within final_depth moves, ids should return the board.


def ids(start_board, goal_board, final_depth):


    ##THIS IS A SINGLE ITERATION OF IDS
    def ids_singleIteration(fringe,final_depth,goal_board,horizon):
        if fringe== []:
            return STOP
        currstate = fringe.pop()
        if currstate.board == goal_board:
            return currstate.board
        if final_depth < 0:
            return None
        while len(fringe)>0:
            if currstate.depth >= horizon:
                return CONTINUE
            else:
                expand_fringe(currstate,fringe)
                return CONTINUE

    #   THIS IS A SOLVER FOR IDS USING singleIteration
    found = False
    fringe = [State.State(start_board,None,0,0)]
    horizon = 0
    while not found and final_depth > 0:
        final_depth -= 1
        found = ids_singleIteration(fringe,final_depth,goal_board,horizon)
    if type(found) is State.State:
        return found
    return None
###########################
# Main method for testing #
###########################


def main():
    ### try for 8 puzzle first
    # 8-Puzzle Tests!
    goal_board = Board.Board([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 0]])

    simple_board = Board.Board([[1, 2, 0],
                              [4, 5, 3],
                              [7, 8, 6]])

    print("This is the board we have:\n")
    print(simple_board)

    # Simple test case for expand_fringe
    fringe1 = []
    node1 = State.State(simple_board, None, 0, 0)
    #so current state is a state made up of simple_board, no parent state, 0 depth, 0 fvalue
    expand_fringe(node1, fringe1)
    assert State.State(simple_board.slide_blank((-1, 0)), node1, 0, 0) not in fringe1
    assert State.State(simple_board.slide_blank((0, -1)), node1, 0, 1) in fringe1
    print("i think expand fringe is working?")

    # Simple test case for breadth_first_search
    fringe1 = []
    node1 = State.State(simple_board, None, 0, 0)
    expand_fringe(node1, fringe1)
    assert breadth_first_search(fringe1, 3, goal_board) == CONTINUE
    fringe1[0] = State.State(goal_board, node1, 0, 0) #what is happening here?
    assert type(breadth_first_search(fringe1, 3, goal_board)) is State.State
    print("this is the board we have after bfs")
    print(simple_board)
    print("i think BFS is working?")

    # Simple test case for ucs_f_function
    node1 = State.State(simple_board, None, 0, 0)
    assert ucs_f_function(node1.board, 0) == 0

    # Simple test case for a_star_f_function
    # -> This checks that the return type is correct
    assert hasattr(a_star_f_function_factory(None, goal_board), '__call__')

    # This section is for you to create tests for your own heuristic

    # Simple test for Informed Expansion
    # node1 = State.State(simple_board, None, 0, 0)
    # fringe1 = []
    # informed_expansion(node1, fringe1, ucs_f_function)
    #assert State.State(simple_board.slide_blank((-1, 0)), node1, 0, 0) not in fringe1
    #assert State.State(simple_board.slide_blank((0, -1)), node1, 0, 1) in fringe1

    # Simple test for Informed Search
    # fringe1 = []
    # explored = {}
    # node1 = State.State(simple_board, None, 0, 0)
    # expand_fringe(node1, fringe1)
    # assert informed_search(fringe1, goal_board, ucs_f_function, explored) == CONTINUE
    # fringe1[0] = State.State(goal_board, node1, 0, 0)
    # assert type(informed_search(fringe1, goal_board, ucs_f_function, explored)) is State.State

    # Simple test for IDS
    node1 = State.State(simple_board, None, 0, 0)
    assert ids(node1.board, goal_board, 1) is None
    result = ids(node1.board, goal_board, 2)
    print(result)
    assert type(result) is Board.Board


    ####

    # 15-Puzzle Tests

    goal_board = Board.Board([[1, 2, 3, 4],
                              [5, 6, 7, 8],
                              [9, 10, 11, 12],
                              [13, 14, 15, 0]])

    simple_board = Board.Board([[1, 2, 3, 0],
                                [5, 6, 7, 4],
                                [9, 10, 11, 8],
                                [13, 14, 15, 12]])
    # print(goal_board)
    # print(simple_board)

    fringe1 = []
    node1 = State.State(simple_board, None, 0, 0)
    expand_fringe(node1, fringe1)
    assert State.State(simple_board.slide_blank((-1, 0)), node1, 0, 0) not in fringe1
    assert State.State(simple_board.slide_blank((0, -1)), node1, 0, 1) in fringe1

    # Simple test case for breadth_first_search
    fringe1 = []
    node1 = State.State(simple_board, None, 0, 0)
    expand_fringe(node1, fringe1)
    assert breadth_first_search(fringe1, 3, goal_board) == CONTINUE
    fringe1[0] = State.State(goal_board, node1, 0, 0)
    assert type(breadth_first_search(fringe1, 3, goal_board)) is State.State

    # Simple test case for ucs_f_function
    node1 = State.State(simple_board, None, 0, 0)
    assert ucs_f_function(node1.board, 0) == 0

    # Simple test case for a_star_f_function
    # -> This ONLY checks that the return type is correct
    assert hasattr(a_star_f_function_factory(None, goal_board), '__call__')

    # This section is for you to create tests for your own heuristic


    # Simple test for Informed Expansion
    node1 = State.State(simple_board, None, 0, 0)
    fringe1 = []
    informed_expansion(node1, fringe1, ucs_f_function)
    assert State.State(simple_board.slide_blank((-1, 0)), node1, 0, 0) not in fringe1
    assert State.State(simple_board.slide_blank((0, -1)), node1, 0, 1) in fringe1

    # Simple test for Informed Search
    fringe1 = []
    explored = {}
    node1 = State.State(simple_board, None, 0, 0)
    expand_fringe(node1, fringe1)
    assert informed_search(fringe1, goal_board, ucs_f_function, explored) == CONTINUE
    fringe1[0] = State.State(goal_board, node1, 0, 0)
    assert type(informed_search(fringe1, goal_board, ucs_f_function, explored)) is State.State

    # Simple test for IDS
    node1 = State.State(simple_board, None, 0, 0)
    assert ids(node1.board, goal_board, 1) == None
    result = ids(node1.board, goal_board, 4)
    assert type(result) is Board.Board


if __name__ == "__main__":
    main()
