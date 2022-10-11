#!/usr/bin/python3

### CSCI-B 351 / COGS-Q 351 Spring 2020
### Framework code copyright 2020 B351/Q351 instruction team.
### Do not copy or redistribute this code without permission
### and do not share your solutions outside of this class.
### Doing so constitutes academic misconduct and copyright infringement.

from board import Board
from player import *

def player_check(trace, depth, expected):
    totalpassedtest = 0

    try:
        print(f"\nMiniMax Test on {trace}, depth {depth}...")
        player = PlayerMM(depth)
        answer = player.findMove(trace)
        if answer == expected:
            print("Passed")
            totalpassedtest +=  1
        else:
            print("Failed")
            print(f"Expect: {expected}, Return: {answer}\n")
    except NotImplementedError:
        print('minimax not implemented.')

    try:
        print(f"\nAlpha/beta pruning Test on {trace}, depth {depth}...")
        player = PlayerAB(depth)
        answer = player.findMove(trace)
        if answer == expected:
            print("Passed")
            totalpassedtest +=  1
        else:
            print("Failed")
            print(f"Expect: {expected}, Return: {answer}\n")
    except NotImplementedError:
        print('alphaBeta not implemented.')

    try:
        print(f"\nDynamic programming Test on {trace}, depth {depth}...")
        player = PlayerDP(depth)
        answer = player.findMove(trace)
        if answer == expected:
            print("Passed")
            totalpassedtest +=  1
        else:
            print("Failed")
            print(f"Expect: {expected}, Return: {answer}\n")
    except NotImplementedError:
        print('PlayerDP not implemented.')

    return totalpassedtest


if __name__ == '__main__':
    ####################################################
    #    Test for findMove() (minimax and alphaBeta)   #
    ####################################################

    # This code allows you to construct tests based on minimax trees you have drawn.
    # Remember that to our algorithms, a win is a win (margin of victory does not matter.)

    # Example: assume we have the heuristic of board.p1_pot - board.p2_pot.
    # (This is trivial enough that you should not even consider using it for real.)
    # Consider the board with trace 123551234220105241 at a depth of 2.

    max_depth = 2
    trace = '123551234220105241'
    BasePlayer.heuristic = lambda self, board: board.p1_pot - board.p2_pot

    #            3   2       0
    #    0   0   6   1   0   8
    # 10                       4
    #    0   0   1   5  10   3

    # P2 has three options: 0, 2, and 3.
    # If P2 picks 0, then we get 1235512342201052410:
    #    1   1   7   2   1   0
    # 11                       4
    #    1   1   1   5  10   3
    #    0   1   2   3   4   5
    # If P1 picks 0, 1, or 2, then the heuristic when we cut off will be 4 - 11 = -7.
    # If P1 picks 3, 4, or 5, then the heuristic when we cut off will be 5 - 11 = -6.
    # So we assign 1235512342201052410 a score of -6.

    # If P2 picks 2, then we get 1235512342201052412:
    #    0   0   7   0   0   8
    # 10                       4
    #    0   0   1   5  10   3
    #            2   3   4   5
    # If P1 picks          2, then the heuristic when we cut off will be 4 - 10 = -6.
    # If P1 picks 3, 4, or 5, then the heuristic when we cut off will be 5 - 10 = -5.
    # So we assign 1235512342201052412 a score of -5.

    # If P2 picks 3, then we get 1235512342201052413:
    #    1   1   0   1   0   8
    # 11                       4
    #    1   1   2   5  10   3
    #    0   1   2   3   4   5
    # If P1 picks 0, 1, or 2, then the heuristic when we cut off will be 4 - 11 = -7.
    # If P1 picks 3, 4, or 5, then the heuristic when we cut off will be 5 - 11 = -6.
    # So we assign 1235512342201052413 a score of -6.

    # Since this is P2's move, we assign 123551234220105241 a score of -6.
    # We expect that P2 will pick move 0, under the usual ordering. Move 3 would be equivalently good.

    expected = 0
    player_check(trace, max_depth, expected)

    # Now it's your turn to try constructing similar tests!
    # THere are many other good ways to come up with testing code, as well.

    ##############################
    #  To write your own TESTS!!! #
    ##############################

    # TESTS you should make by yourself:
    # 1. Check for handling draw in endgame.
    #    You should have a case for handling boards which have no winner (each player gets 24 stones).
    #
    # 2. Check for tie in minimax and alphabeta functions:
    #    You should have a case to break tie if there are two moves that is equally good (should be first considered move)
    #
    # 3. Check that your heuristic always falls strictly within your P2_WIN, P1_WIN range.
