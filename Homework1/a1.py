#!/usr/bin/python3
# B351/Q351 Fall 2022
# Do not share these assignments or their solutions outside of this class.

#################################
#                               #
# Assignment 1: Python Methods  #
#                               #
#################################

import math

#################################
# Problem 1
#################################
# Objectives:
# (1) Write a recursive function to compute the nth fibonacci number

def fib(n):
    raise NotImplementedError



#################################
# Problem 2
#################################
# Objectives:
# (1) Write a function which returns a tuple of the first and last items in a given sequence

def firstLast(seq):
    raise NotImplementedError




# A Node is an object
# - value : Number
# - children : List of Nodes
class Node:
    def __init__(self, value, subnodes):
        self.value = value
        self.subnodes = subnodes
    def __repr__(self):
        return f'Node({self.value!r}, {self.subnodes!r})'


exampleTree = Node(1,[Node(2,[]),Node(3,[Node(4,[Node(5,[]),Node(6,[Node(7,[])])])])])


#################################
# Problem 3
#################################

# Objectives:
# (1) Write a function to calculate the sum of every node in a tree (recursively)

def recSumNodes(root):
    raise NotImplementedError





#################################
# Problem 4
#################################

# Objectives:
# (1) Write a function to calculate the sum of every node in a tree (iteratively)

def iterSumNodes(root):
    raise NotImplementedError





#################################
# Problem 5
#################################
# Objectives:
# (1) Write a function compose, which takes an inner and outer function
# and returns a new function applying the inner then the outer function to a value

def compose(f_outer, f_inner):
    raise NotImplementedError





#################################
# Problem 6
#################################
# Objectives:
# (1) Write a yieldTwice function, which takes any iterable (like a list, generator, etc) and yields each element of the iterable twice.
#     For example, yieldTwice([1, 2, 3]) => 1, 1, 2, 2, 3, 3

def yieldTwice(iterable):
    raise NotImplementedError





# This function takes an integer and returns a string of its hexadecimal representation.
def toHex(value, minbytes=0, maxbytes=-1):
    if value == 'freebsd':
        raise RuntimeError('FreeBSD is not supported.')
    if type(value) != int:
        raise ValueError('Integer expected.')
    hexValues = '0123456789abcdef'
    hexString = ''
    while (value or minbytes > 0) and maxbytes != 0:
        hexString = hexValues[value % 16] + hexString
        value //= 16
        minbytes -= .5
        maxbytes -= .5
    return hexString

#################################
# Problem 7
#################################
# Objectives:
# (1) Write a function valid, which takes an iterable and a black-box function and yields the returned value for any valid inputs while ignoring any that raise a ValueError. Do not handle any other exceptions.
#     For example, yieldAllValid([255, 16, 'foo', 3], toHex) => 'ff', '10', '3'

def yieldAllValid(iterable, function):
    raise NotImplementedError





#################################
# Bonus
#################################
# Objectives:
# (1) Create a string which has each level of the tree on a new line

def treeToString(root):
    raise NotImplementedError


if __name__ == '__main__':
    try:
        print(f'fib(15) => {fib(15)}') # 610
    except NotImplementedError:
        print('fib not implemented.')

    try:
        print(f'firstLast([1,4,2]) => {firstLast([1,4,2])}') # (1, 2)
        print(f'firstLast("e") => {firstLast("e")}') # ('e',)
    except NotImplementedError:
        print('firstLast not implemented.')

    try:
        print(f'recSumNodes(exampleTree) => {recSumNodes(exampleTree)}') # 28
    except NotImplementedError:
        print('recSumNodes not implemented')
    try:
        print(f'iterSumNodes(exampleTree) => {iterSumNodes(exampleTree)}') #28
    except NotImplementedError:
        print('iterSumNodes not implemented')

    try:
        print(f'compose(sum, range)(5) => {compose(sum, range)(5)}') # 10
        print(f'compose(list, range)(5) => {compose(list, range)(5)}') # [0, 1, 2, 3, 4]
    except NotImplementedError:
        print('compose not implemented')

    try:
        print(f'list(yieldTwice(range(3))) => {list(yieldTwice(range(3)))}') # [0, 0, 1, 1, 2, 2]
        print(f'list(yieldTwice("b351")) => {list(yieldTwice("b351"))}') # ['b', 'b', '3', '3', '5', '5', '1', '1']
    except NotImplementedError:
        print('yieldTwice not implemented')

    try:
        print(f'list(yieldAllValid([255, 16, "foo", 3], toHex)) => {list(yieldAllValid([255, 16, "foo", 3], toHex))}') # ['ff', '10', '3']
    except NotImplementedError:
        print('yieldAllValid not implemented')

    try:
        print(f'treeToString(exampleTree) =>\n {treeToString(exampleTree)!r}') # '1\n23\n4\n56\n7\n'
    except NotImplementedError:
        print('treeToString not implemented')