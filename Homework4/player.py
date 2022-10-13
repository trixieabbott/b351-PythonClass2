#!/usr/bin/python3

### CSCI-B 351 / COGS-Q 351 Spring 2020
### Framework code copyright 2020 B351/Q351 instruction team.
### Do not copy or redistribute this code without permission
### and do not share your solutions outside of this class.
### Doing so constitutes academic misconduct and copyright infringement.

import math
from board import Board
import random

class BasePlayer:
    def __init__(self, max_depth):
        self.max_depth = max_depth

    ##################
    #      TODO      #
    ##################
    # Assign integer scores to the three terminal states
    # P2_WIN_SCORE < TIE_SCORE < P1_WIN_SCORE
    # Access these with "self.TIE_SCORE", etc.
    P1_WIN_SCORE = 2000
    P2_WIN_SCORE = -2000
    TIE_SCORE =  0

    # Returns a heuristic for the board position
    # Good positions for player 1 pieces should be positive and
    # good positions for player 2 pieces should be negative
    # for all boards, P2_WIN_SCORE < heuristic(b) < P1_WIN_SCORE
    #CAN BE NEGATIVE, IF IT'S POSITIVE, I AM CLOSER TO WINNING
    #Understand tic tac toe heuristic
    
    def heuristic(self, board):
        score = (board.p1_pot - board.p2_pot) * 15
        ## game over :( or :) maybe?
        if board.p1_pot > 25 or board.p2_pot > 25:
            return 1999 if board.p1_pot > 25 else -1999
        ## hoarder
        score += sum([(3-i)*board.p1_pits[i-1] for i in range(3)])
        score += sum(board.p1_pits)
        score -= sum([(3-i)*board.p2_pits[i-1] for i in range(3)])
        score -= sum(board.p2_pits)
        for i in range(6):
            ## captures
            pit = i if not board.turn else i + 7
            stones = board.board[pit]
            while stones > 0:
                if (pit == 5 and board.turn) or (pit == 12 and not board.turn):
                    pit += 2
                else: pit += 1
                pit %= 14
                stones -= 1
            new_side = pit // 7
            if board.turn == new_side and not board.board[pit] and board.board[12-pit]:
                score += (board.board[12-pit] + 1) * (1 - board.turn*2)
        return score

    def findMove(self, trace):
        raise NotImplementedError

class ManualPlayer(BasePlayer):
    def __init__(self, max_depth=None):
        BasePlayer.__init__(self, max_depth)

    def findMove(self, trace):
        board = Board(trace)
        opts = "  "
        for c in range(6):
            opts += " "+(str(c+1) if board.isValidMove(c) else ' ')+"  "

        while True:
            if(board.turn == 0):
                print("\n")
                board.printSpaced()
                print(opts)
                pit = input("Pick a pit (P1 side): ")
            else:
                print("\n")
                print(" " + opts[::-1])
                board.printSpaced()
                pit = input("Pick a pit (P2 side): ")
            try: pit = int(pit) - 1
            except ValueError: continue
            if board.isValidMove(pit):
                return pit

class RandomPlayer(BasePlayer):
    def __init__(self, max_depth=None):
        BasePlayer.__init__(self, max_depth)
        self.random = random.Random(13487951347859)
    def findMove(self, trace):
        board = Board(trace)
        options = list(board.getAllValidMoves())
        return self.random.choice(options)

class RemotePlayer(BasePlayer):
    def __init__(self, max_depth=None):
        BasePlayer.__init__(self, max_depth)
        self.instructor_url = "http://silo.cs.indiana.edu:30005"
        if self.max_depth > 8:
            print("It refused to go that hard. Sorry.")
            self.max_depth = 8
    def findMove(self, trace):
        import requests
        r = requests.get(f'{self.instructor_url}/getmove/{self.max_depth},{trace}')
        move = int(r.text)
        return move


class PlayerMM(BasePlayer):
    ##################
    #      TODO      #
    ##################
    # performs minimax on board with depth.
    # returns the best move and best score as a tuple
    def minimax(self, board, depth):
        #TODO
        winner = board.winner 
        if (winner is not None): #BASE CASE
            if(winner == 0):
                return (None, self.P1_WIN_SCORE)
            if(winner == 1):
                return (None, self.P2_WIN_SCORE)
            if(winner == -1):
                return (None, self.TIE_SCORE)
        if depth == 0:
            return (None, self.heuristic(board))

        #ELSE..
        if(board.turn == 0): #if it's player 1's turn
            bestScore = self.P2_WIN_SCORE - 1
            bestMove = -1
            for move in board.getAllValidMoves():
                board.makeMove(move)
                _, score = self.minimax(board, depth - 1)
                board.undoMove()
                if(score > bestScore):
                    bestScore = score
                    bestMove = move
            return (bestMove, bestScore)

        
        else: #if it's player 2's turn 
            bestScore = self.P1_WIN_SCORE + 1
            bestMove = -1
            for move in board.getAllValidMoves():
                board.makeMove(move)
                _, score = self.minimax(board, depth - 1)
                board.undoMove()
                if(score < bestScore):
                    bestScore = score
                    bestMove = move
            return (bestMove, bestScore)

    def findMove(self, trace):
        board = Board(trace)
        move, score = self.minimax(board, self.max_depth)
        return move

class PlayerAB(BasePlayer):
    ##################
    #      TODO      #
    ##################
    # performs minimax with alpha-beta pruning on board with depth.
    # alpha represents the score of max's current strategy
    # beta  represents the score of min's current strategy
    # in a cutoff situation, return the score that resulted in the cutoff
    # returns the best move and best score as a tuple
    def alphaBeta(self, board, depth, alpha, beta):
        winner = board.winner
        if (winner is not None): #BASE CASE
            if(winner == 0):
                return (None, self.P1_WIN_SCORE)
            if(winner == 1):
                return (None, self.P2_WIN_SCORE)
            if(winner == -1):
                return (None, self.TIE_SCORE)
        if depth == 0:
            return (None, self.heuristic(board))

        #ELSE
        if(board.turn == 0):
            bestScore = self.P2_WIN_SCORE - 1
            bestMove = -1
            for move in board.getAllValidMoves():
                board.makeMove(move)
                _, v = self.alphaBeta(board, depth - 1, alpha, beta)
                board.undoMove()

                if(v > bestScore):
                    bestScore = v
                    bestMove = move
                alpha = max(alpha, v)
                if alpha >= beta: #where pruning happens
                    return (None, v)
                if(bestScore == self.P1_WIN_SCORE):
                    return (bestMove, bestScore)
            return (bestMove, bestScore)
        else:
            bestScore = self.P1_WIN_SCORE + 1
            bestMove = -1
            for move in board.getAllValidMoves():
                board.makeMove(move)
                _, v = self.alphaBeta(board, depth - 1, alpha, beta)
                board.undoMove()

                if(v < bestScore):
                    bestScore = v
                    bestMove = move
                beta = min(beta, v)
                if alpha >= beta:
                    return (None, v)
                if(bestScore == self.P2_WIN_SCORE):
                    return (bestMove, bestScore)
            return (bestMove, bestScore)

    def findMove(self, trace):
        board = Board(trace)
        move, score = self.alphaBeta(board, self.max_depth, -math.inf, math.inf)
        return move

class PlayerDP(PlayerAB):
    ''' A version of PlayerAB that implements dynamic programming
        to cache values for its heuristic function, improving performance. '''
    def __init__(self, max_depth):
        PlayerAB.__init__(self, max_depth)
        self.resolved = {}

    ##################
    #      TODO      #
    ##################
    # if a saved heuristic value exists in self.resolved for board.state, returns that value
    # otherwise, uses BasePlayer.heuristic to get a heuristic value and saves it under board.state
    def heuristic(self, board):
        if board.state in self.resolved:
            return self.resolved[board.state]
        else:
            hValue = BasePlayer.heuristic(self,board)
            self.resolved.update({board.state: hValue})
            return hValue


class PlayerBonus(BasePlayer):
    ''' This class is here to give you space to experiment for your ultimate Mancala AI,
        your one and only PlayerBonus. This is only used for the extra credit tournament. '''
    def findMove(self, trace):
        raise NotImplementedError

#######################################################
###########Example Subclass for Testing
#######################################################

# This will inherit your findMove from above, but will override the heuristic function with
# a new one; you can swap out the type of player by changing X in "class TestPlayer(X):"
class TestPlayer(BasePlayer):
    # define your new heuristic here
    # Assign integer scores to the three terminal states
    # P2_WIN_SCORE < TIE_SCORE < P1_WIN_SCORE
    # Access these with "self.TIE_SCORE", etc.
    P1_WIN_SCORE = 50
    P2_WIN_SCORE = -50
    TIE_SCORE =  0
    def heuristic(self):
        #IDEAS
        #if its player 1's turn -->  add 10
        
        #if its player 2's turn --> subtract 10
        

        #if player 1 has mores stones -> add 5 to them?

        #if player 2 has more stones --> subtract 5?

        #if player 1 has 1 stone in 6th pit, 2 stones in 5th pit, etc. --> add 5

        #if player 2 has 1 stone in 6th pit, 2 stones in 5th pit, etc. --> subtract 5


        #if player 1 has empty spots, and theres stones across the way,  add 5

        # if player 2 has empty spots, and theres stones accross the way, add 5
        pass

        # score = (board.p1_pot - board.p2_pot) * 15
        # ## game over :( or :) maybe?
        # if board.p1_pot > 25 or board.p2_pot > 25:
        #     return 1999 if board.p1_pot > 25 else -1999
        # ## hoarder
        # score += sum([(3-i)*board.p1_pits[i-1] for i in range(3)])
        # score += sum(board.p1_pits)
        # score -= sum([(3-i)*board.p2_pits[i-1] for i in range(3)])
        # score -= sum(board.p2_pits)
        # for i in range(6):
        #     ## captures
        #     pit = i if not board.turn else i + 7
        #     stones = board.board[pit]
        #     while stones > 0:
        #         if (pit == 5 and board.turn) or (pit == 12 and not board.turn):
        #             pit += 2
        #         else: pit += 1
        #         pit %= 14
        #         stones -= 1
        #     new_side = pit // 7
        #     if board.turn == new_side and not board.board[pit] and board.board[12-pit]:
        #         score += (board.board[12-pit] + 1) * (1 - board.turn*2)
        # return score



