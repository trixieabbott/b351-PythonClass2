import math
import random as rn

# Name of your programmig partner
# Name: 

# Problem 1
# Recursive functions
# Implement the recursion as per the equations shown in Problem-1 in HW PDF 
# for each of the functions below.
def s(n):
    if n == 0:
        return 0
    else:
        return s(n-1) + n

def p(n):
    if n == 0:
        return 10000
    else:
        return p(n-1) + 0.02*p(n-1)

def b(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return b(n-1) + b(n-2)


def c(n):
    if n == 1:
        return 9
    else:
        return 9*c(n-1) + 10**(n-1) - c(n-1)

def d(n):
    if n == 0:
        return 1
    else:
        return 3*d(n-1) + 1


# Problem 2
# Implement via equation 19 in HW PDF.
def min(x,y):
    if x<y:
        return x
    else:
        return y

# Implement via equation 20-21 as per the instructios in the PDF.
def MIN(lst):
    if len(lst)==1:
        return lst[0]
    else:
        return min(lst[0],MIN(lst[1:]))




# Problem 3
# Input: A string in hexadecimal format
# Output: The deciaml (integer) equivalent of the input
def hex_dec(hex):
    u = hex.upper()
    val = {'O':0, '1':1, '2':2, '3':3, '4':4,'5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    power = len(hex) - 1
    dec = 0 
    for i in u:
        dec = dec + val[i]
        power -= 1
    return dec

    

# Problem 4
# Input: A number (decimal format) and base
# Output: The string representation of the converted number in base.
def c_(dn, base):
    if (dn == 0):
        return ""
    if (dn == 1):
        return "1"
    else:
        return c_(dn//base, base) + str(dn % base)
    
    for i in range(1,14):
        b2,b3,b4 = c_(i,2), c_(i,3), c_(i,4)
        print(f"{int(b2,2)} {b2},{int(b3,3)}{b3},{int(b4,4)} {b4}")


# Problem 5
# Input: An object x and a list
# Output: List with all occurences of x removed
def rr(x,lst):
    y = 0
    if lst == []:
        return []
    else:
        if lst[y] == x:
            return rr(x,lst[y+1:])
        else:
            return [lst[y]] + rr(x,lst[y+1:])


# Input: An object x, non-negative number n, and a list
# Output: A boolean indicating if x appeared at-least n times or not in the list
def oal(x, n, lst):
    # Create your local function here o_() and call it with required arguments.
    # You can use the value returned by o_(), as the final return value of oal() as well.
    pass


# Problem 6
# Implement a non-arcane recursive version of mystic
def mystic(xstr):
    if len (xstr) == 1:
        return True 
    elif len(xstr) == 2 and xstr[0] == xstr[1]:
        return True 
    else:
        if xstr[0] == xstr[len(xstr)-1]:
            if mystic(xstr[1:len(xstr)-1]) == True:
                return True 
            else:
                return False
        else:
            return False


# Problem 7
# Implement the recursion as per the HW PDF instructions.
def A(m, n):
    if (m==0):
        return n + 1
    elif (n == 0):
        return A(m,1)
    else:
        return A(m,A(m+1,n))
 

# Problem 8
# Input: x and stop
# Output: Approximated value of sin(x) until stop
def ii(x, stop):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    
    sum = 0
    i = 0
    while i <= stop: 
        if i % 2 == 0:
            sum += ((1**i) * ((x**(2*i + 1))/factorial((2*i)+1)))
        else:
            sum += ((-1**i) * ((x**(2*i + 1))/factorial((2*i)+ 1)))
        i += 1
    return sum 

# Implement as per HW pdf instructions.
# Will produce output equal to equation-32 but with loop.
def iii(stop):
    def closed(n):
        return (1/4)*(n**2)*(n+1)**2
    sum = 0
    for i in range(1,stop+1):
        sum += (i)**3
    return [round(int(sum),2),round(closed(stop),2)]

# Implement as per HW pdf instructions.
# Will produce output equal to equation-33 but with loop.
def iv(stop):
    def closed(n):
        return (1/2)*n*(6*(n**2)-(3*n)-1)
    sum = 0
    for i in range(1,stop +1):
        sum += ((3*i)-2)**2
    return [round(int(sum),2), round(closed(stop),2)]

# Implement as per HW pdf instructions. 
# Will produce output equal to equation-34 but with loop. 
def vi(x,stop):
    def closed(x,n):
        return math.sin(x*(2**n))/((2**n)*math.sin(x))
    prod = 1
    for i in range(1,stop+1):
        prod = prod * math.cos(x*(2*(i-1)))
    return [round(prod,2),round(closed(x,stop),2)]


# Problem 9
# Implement the model as per the instructions in HW PDF.
def I(t):
    return ((5* t** 2 + t + 400)/(2 * t**2 + 2*t + 90))

# Implement the model as per the instructions in HW PDF.
def J(t):
    data = [60.0, 59.0, 58.0, 55.26, 53.85, 52.17, 51.55, 49.00, 46.26, 43.52, 50.76]
    return data[t]

# Implement the model as per the instructions in HW PDF.
def K(t):
    return (50* t**2 + 600/t**2 + 10)

# Input: a model
# Output: List of months and quality index for those months (formatted as per the output in HW PDF)
def env(f):
    
    months = ["Jan", "Feb", "Mar", "Apr", "May",
              "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    pass


# Problem-10 is not graded.

# Uncomment the below code to see the graphical output cretaed by Pygame
# You are expected to understand the code because this will be needed in the next HW

# If the code does not run in VSC (and complaints about pygame module not found) then you can also run it
# by changing the directory to Assignment6 and running it manually as follows:

# Open a new Terminal in VSC (change directory to Assignment6) 
# cd Assignment6 (cd command is used to change directory to Assignment6)

# Run the a6.py as follows
# python3 a6.py (you have already seen this before in labs)

# This should show the pygame window with a triangle

# REMEMBER TO COMMENT ALL CODE FOR PROBLEM 10 before submitting to AUOTOGRADER (only for problem 10).
# Otherwise, it would return with an error. This is because the Autograder can't run graphical outputs for you
# as of now. 

# So, once you are understand the code, have run it a few times, comment it back. 

# For some of you, at-first it may be puzzling that nothing is happening, look out for a small
# graphical window, it may show behind your VSC window, so you may have to minimize VSC to look at it.
# Press the 'cross' button to close that window.

# REMEMBER TO COMMENT ALL CODE FOR PROBLEM 10 before submitting to AUOTOGRADER (only for problem 10).

##########################
# Problem 10 code starts here
##########################


# pygame.init()

# BLUE = (0,0,255)
# WHITE = (255,255,255)

# DISPLAYSURF = pygame.display.set_mode((500, 500), 0, 32)

# pygame.display.set_caption('I love C200! My first triangle')

# #INPUT takes a location loc = (x,y) pair of points and width
# #RETURN 3 points of the equilateral triangle determined by loc and width
# def triangle(loc,width):
#     x,y = loc
#     z = math.sqrt(width**2 - (width/2))
#     return (x,y),(x - width/2,y + z),(x + width/2, y + z)

# DISPLAYSURF.fill(WHITE)

# #Draws Triangle
# #(triangle(loc,w)) is a tuple of tuples...)
# def draw_triangle(loc, w):
#     pygame.draw.polygon(DISPLAYSURF, (rn.randint(0,255),rn.randint(0,255),rn.randint(0,255)) , (triangle(loc,w)),1)

# #INPUT location and width
# #RETURN nothing (preparing for next week)
# def s(loc,width):
#     draw_triangle(loc,width)
    
# #calls draw triangle once
# #top is at 240,0 width = 440
# s((240,0),440)

# while True:
#     for event in pygame.event.get():
#          if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()


##########################
# Problem 10 code ends here
##########################


if __name__ == "__main__":
    '''
    Please add some of your own tests too for good testing
    '''
    #Problem 1
    print(f"    s, p,     d")
    for i in range(10):
       print(f"{i}: {s(i),p(i),d(i)}")
    print(f"    b, c")
    for i in range(1,10):
        print(f"{i}: {b(i),c(i)}")
    # s, p,     d
    # 0: (0, 10000, 1)
    # 1: (1, 10200.0, 4)
    # 2: (3, 10404.0, 13)
    # 3: (6, 10612.08, 40)
    # 4: (10, 10824.3216, 121)
    # 5: (15, 11040.808031999999, 364)
    # 6: (21, 11261.62419264, 1093)
    # 7: (28, 11486.8566764928, 3280)
    # 8: (36, 11716.593810022656, 9841)
    # 9: (45, 11950.925686223109, 29524)
    #     b, c
    # 1: (2, 9)
    # 2: (3, 82)
    # 3: (5, 756)
    # 4: (8, 7048)
    # 5: (13, 66384)
    # 6: (21, 631072)
    # 7: (34, 6048576)
    # 8: (55, 58388608)
    # 9: (89, 567108864)

    #problem 2
    # prob2 = [[0,1,-1],[10],[11,10,9,8]]
    # for i in prob2:
    #     print(f"{i} {MIN(i)}")
    # [0, 1, -1] -1
    # [10] 10
    # [11, 10, 9, 8] 8

    #problem 3
    # prob3 = ['c1',"C1","7De","7dE","10F"]
    # for i in prob3:
    #     print(f"{i} {hex_dec(i)} {int(i,16)}") 
    # c1 193 193
    # C1 193 193
    # 7De 2014 2014
    # 7dE 2014 2014
    # 10F 271 271

    #problem 4
    # for i in range(14):
    #     b2,b3,b4 = c_(i,2),c_(i,3),c_(i,4)
    #     print(f"{int(b2,2)} {b2}, {int(b3,3)} {b3}, {int(b4,4)} {b4}")

    #problem 5
    # lst = [1,1,1,2,2,0]
    # print(rr(1,lst))
    # for i in [4,3,1]:
    #     print(oal(1,i,lst))

    #problem 6
    # data = ["ABBa","ratsliveonnoevilstar", "ATOYOTA","ccc","cc","ccedc",]
    # for d in data:
    #     print(mystic(d))

    #problem 7
    # for i in range(4):
    #     for j in range(4):
    #         print(f"A({i,j}) = {A(i,j)},  ", end="")
    ###when you have time: print(A(4,1))

    #problem 8
    # x,stop = math.pi/4,5
    # print(ii(x,stop))
    # print(math.sin(x))
    # print(iii(5))
    # print(iv(5))
    # print(vi(math.pi,5))

    #problem 9
    # print("Model I:\n", env(I))
    # print("Model J:\n", env(J))
    # print("Model K:\n", env(K))