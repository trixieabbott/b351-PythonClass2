import os
# print(f"Current: {os.getcwd()}")
# os.chdir("D:\\C200\Data")
# print(f"Current: {os.getcwd()}")

###############
# PROBLEM ONE
###############

#choice
def C(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return C(n-1, k) + C(n-1, k-1)

def B(n):
    if n == 0:
         return 1
    else:
        coeficient = 1/(n+1)
        lst = []
        for k in range(n):
            lst.append(C(n+1, k)*B(k))
        return -coeficient*(sum(lst))
        
 
###############
# PROBLEM TWO
###############
def a(n):
    if n <= 0:
        return 2
    elif n == 1:
        return 3
    elif n == 2:
        return 5
    else:
        return a(n-1) + a(n-2) + a(n-3)

def aw(n):
    v0,v1,v2 =2,3,5
    while n != 0:
        v0,v1,v2 = v1,v2,v0+v1+v2
        n -= 1
    return v0

def a_gen():
    v0,v1,v2 =2,3,5
    while True:
        yield v0
        v0,v1,v2 = v1,v2,v0+v1+v2

def at(n,v0=2,v1=3,v2=5):
    if n <= 0:
        return v0
    elif n == 1:
        return v1
    elif n == 2:
        return v2
    else:
        return at(n-1,v1,v2,v0 + v1 + v2)


def bb(x):
    if x == 0:
        return 2
    elif x == 1:
        return -3
    else:
        return bb(x-1)*bb(x-2) 

def bbw(x):
    v0,v1 = 2,-3
    while x != 0:
        v0,v1 = v1,v0*v1
        x -= 1
    return v0

def bb_gen():
    v0,v1 = 2,-3
    while True:
        yield v0
        v0,v1 = v1,v0*v1

def bbt(x,v0=2,v1=-3):
    if x == 0:
        return v0
    elif x == 1:
        return v1
    else:
        return bbt(x-1,v1,v0*v1)

def F(n,m,p):
    if p == 0:
        return 100 + n - m
    else:
        return n*m - p + F(n-3, m-2,p-1)

def Ft(n,m,p,v = 100):
    if p == 0:
        return v + n - m
    else:
        return Ft(n-3,m-2,p-1, n*m - p + v )

def Fw(n,m,p):
    v = 0
    while p:
        v += m*n - p
        n,m,p = n-3,m-2,p-1
    return v + 100 + n - m 

def m(x,y):
    if x <= 0 and y <= 0:
        return 3
    elif x <= 0:
        return 2
    elif y <= 0:
        return 1
    else:
        return m(x-1,y-1) + m(x-1,y-2)
    
def mw(x,y):
    d = {(0,0):3,(0,1):2,(1,0):1}
    def on_edge(x,y):
        if x <= 0 and y <= 0:
            return 3
        if x <= 0:
            return 2
        elif y <= 0:
            return 1
    i = 0
    while i <= x:
        j = 0
        while j <= y:
            if on_edge(i,j):
                d[(i,j)] = on_edge(i,j)
            else:
                if on_edge(i-1,j-1): # and not (i-1,j-1) in d.keys():
                    d[(i-1,j-1)] = on_edge(i-1,j-1)
                if on_edge(i-1,j-2): # and not (i-1,j-2) in d.keys():
                    d[(i-1,j-2)] = on_edge(i-1,j-2)
                d[(i,j)] = d[(i-1,j-1)] + d[(i-1,j-2)]
            j += 1
        i += 1
    return d[(i-1,j-1)]


###############
# PROBLEM THREE
###############
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np

#INPUT takes path + filename
#RETURN returns list of tuples [(year,population),...]
def get_data(path,name):
    with open(path + name, 'r') as file:
        data = file.readlines()
        
        # print(data)
        d_list = []
        for line in data[1:]:
            s_line = line.strip('\n')
            y, p = s_line.split(" ")
            d_list.append((int(y),int(p)))
        return d_list

def pop(year):
    return 1436.53*(1.01395**year)

def error(data):
    sum = 0
    tmp = []
    for y,p in data:
        v = abs(p - pop(y))
        sum += v
        tmp += [v]
    return (1/(len(data)))*sum


###############
# PROBLEM four
###############
#You cannot simply divide or use modulus
#You must implement the algorithm as described
def div_11(n):
    sum = 0
    i = 1
    while n > 10:
        sum += (n % 10)*((-1)**i)
        n = n // 10
        i = 1 - i
    v = abs(sum + n*((-1)**i)) 
    return (v == 11) or (v == 0)

###############
# PROBLEM five
###############
#INPUT list of numbers
#RETURN list of nesting level and sum at that level
def sl(lst,p=0):
   v = 0
   if lst:
      tmp = []
      for i in lst:
         if isinstance(i,list):
            tmp += i
         else:
            v += i
      return [[p, v]] + sl(tmp,p+1)
   else:
      return []

#PROBLEM 6

# import pygame, sys
# import math
# from pygame.locals import *
# import random as rn
# pygame.init()

# BLUE = (0,0,255)
# WHITE = (255,255,255)
# BLACK = (0,0,0)

# DISPLAYSURF = pygame.display.set_mode((500, 500), 0, 32)

# pygame.display.set_caption('S-Triangle')

# #INPUT takes a location loc = (x,y) pair of points and width
# #RETURN 3 points of the equilateral triangle determined by loc and width
# def triangle(loc,width):
#     x,y = loc
#     z = math.sqrt(width**2 - (width/2))
#     return (x,y),(x - width/2,y + z),(x + width/2, y + z)

# DISPLAYSURF.fill(BLACK)

#Draws Triangle
#(triangle(loc,w)) is a tuple of tuples...)
# def draw_triangle(loc, w):
#     pygame.draw.polygon(DISPLAYSURF, (rn.randint(0,255),rn.randint(0,255),rn.randint(0,255)) , (triangle(loc,w)),1)


#INPUT location and width
#RETURN nothing -- follows algorithm
#Draw the three smaller triangles as described
#in the text
# def s(loc,width):
#     if width > 1:
#         x,y = loc
#         z = math.sqrt(width**2 - (width/2))
#         draw_triangle(loc,width)
#         s(loc,width/2)
#         s((x-width/4,y + z/2),width/2)
#         s((x + width/4,y + z/2),width/2)
#     else:
#         return


if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    # """

    #PROBLEM 1
    
    # for i in range(6):
    #     print("B({0}) = {1}".format(i,B(i)))

    #PROBLEM 2
    # for i,j in zip(range(10),a_gen()):
    #     print(f"a({i}) {a(i)} {aw(i)} {at(i)} {j} \n",end="")   
    # for i,j in zip(range(10),bb_gen()):
    #     print(f"b({i}) {bb(i)} {bbw(i)} {bbt(i)} {j}")    
    # for i in range(6):
    #     for j in range(6):
    #         for k in range(6):
    #             print(f"{i,j,k} {F(i,j,k)} {Ft(i,j,k)} {Fw(i,j,k)}")
    # for i in range(10):
    #     for j in range(10):
    #         print(f"{i,j} {m(i,j)} {mw(i,j)} ")

#PROBLEM 6

import pygame, sys
import math
from pygame.locals import *
import random as rn
pygame.init()

BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

DISPLAYSURF = pygame.display.set_mode((500, 500), 0, 32)

pygame.display.set_caption('S-Triangle')

#INPUT takes a location loc = (x,y) pair of points and width
#RETURN 3 points of the equilateral triangle determined by loc and width
def triangle(loc,width):
    x,y = loc
    z = math.sqrt(width**2 - (width/2))
    return (x,y),(x - width/2,y + z),(x + width/2, y + z)

DISPLAYSURF.fill(BLACK)

#Draws Triangle
#(triangle(loc,w)) is a tuple of tuples...)
def draw_triangle(loc, w):
    pygame.draw.polygon(DISPLAYSURF, (rn.randint(0,255),rn.randint(0,255),rn.randint(0,255)) , (triangle(loc,w)),1)


#INPUT location and width
#RETURN nothing -- follows algorithm
#Draw the three smaller triangles as described
#in the text
def s(loc,width):
    if width > 1:
        x,y = loc
        z = math.sqrt(width**2 - (width/2))
        draw_triangle(loc,width)
        #s(loc1,width/2)
        #s(loc2,width/2)
        #s(loc2,width/2)
        s(loc,width/2)
        s((x-width/4,y + z/2),width/2)
        s((x + width/4,y + z/2),width/2)
    else:
        return

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the `test_a7.py`. Feel free to add print statements. 
    # """

    #PROBLEM 1
    
    # for i in range(6):
    #     print("B({0}) = {1}".format(i,B(i)))

    #PROBLEM 2
    # for i,j in zip(range(10),a_gen()):
    #     print(f"a({i}) {a(i)} {aw(i)} {at(i)} {j} \n",end="")   
    # for i,j in zip(range(10),bb_gen()):
    #     print(f"b({i}) {bb(i)} {bbw(i)} {bbt(i)} {j}")    
    # for i in range(6):
    #     for j in range(6):
    #         for k in range(6):
    #             print(f"{i,j,k} {F(i,j,k)} {Ft(i,j,k)} {Fw(i,j,k)}")
    # for i in range(10):
    #     for j in range(10):
    #         print(f"{i,j} {m(i,j)} {mw(i,j)} ")

    #Problem 3
    # data = get_data(".", "pop.txt")
    # print(f"data from file:",data)
    # print(f"abs(3040 - {pop(60)}) = {abs(3040 - pop(60))}")
    # ave_error = round(error(data),2)
    # print(f"Average error: {ave_error}")

    # #uncomment to see plot
    # t = np.arange(0.0, 120.0)
    # fig,ax = plt.subplots()

    # ax.plot(t, pop(t),'g')
    # for y,p in data:
    #     ax.plot(y,p,'ro--')

    # ax.set(xlabel ="Time (Year + 1900)", ylabel=r"Pop size $\times 10^6$",
    # title = "Population Model Average Error = {0}".format(ave_error))
    # ax.grid()
    # plt.show()

    #problem 4
    # nlst = [587657752,11,22,2728,31415,1358016]
    # for n in nlst:
    #     print(div_11(n), n / 11)

    #problem 5
    # prob5 = [[1,4,[3,[100]],3,2,[1,[101,1000],5],1,[7,9]],
    #          [1,2,3,4,[10,20,30,40,[100,200,300,400]]],
    #          [[[[100,200,300,400]]],[[10,20,30,40]],1,2,3,4]]
    # for lst in prob5:
    #     print(sl(lst))

    #Problem 6
    s((240,0),440)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()