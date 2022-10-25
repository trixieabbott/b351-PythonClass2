from cmath import log10
import math

#Problem 1
#INPUT list of 0 and 1
#RETURN the COUNT of the longest sequence of concecutive 1s is returned
def ls(x):
    longest = 0
    last_value = 0
    for a in x:
        if a == 1:
            last_value += 1
            if last_value >= longest:
                longest = last_value
        elif a == 0:
            if longest >= last_value:
                last_value = 0
            elif last_value >= longest:
                longest = last_value
                last_value = 0

    return (longest)



###########################################################################
# Problem 2
###########################################################################

#INPUT two lists of 0s and 1s. Think of each list as representing a person
# as explained in the HW PDF.
#RETURN inner product.
def inner_prod(v0, v1):
    a = 0
    for i in range(0, len(v0)):
        a += v0[i]*v1[i]
    return a

#INPUT a list of 0s, 1s
#RETURN square root of inner product
def mag(v):
    return inner_prod(v,v)**(1/2)

#INPUT two lists of 0s, 1s 
#RETURN angle in degrees
def angle(v0, v1):
    a = math.acos(inner_prod(v0,v1)/(mag(v0)*mag(v1)))
    return round(a*(180/math.pi), 2)

#INPUT list of people
#RETURN unique pairs with angle
def match(people):
    peoplelist = []
    for i in range(0,len(people)-1):
        for j in range( i+1, len(people)):
            newlist = []
            angl=angle(people[i], people[j])
            
            newlist.append(people[i])
            newlist.append(people[j])
            newlist.append(angl)
            peoplelist.append(newlist)

    return peoplelist 


#INPUT list of pairs with angle
#RETURN best pair (smallest angle)
def best_match(scores):
    bestm = scores[0][2]
    for i in range(0, len(scores)):
        if bestm > scores[i][2]:
            bestm = scores[i][2]
    for j in range(0, len(scores)):
        if bestm == scores[j][2]:
            return [scores[j][0], scores[j][1], scores[j][2]]


###########################################################################
# Problem 3
###########################################################################
#INPUT two lists like [m ,b]. Each list represents a line in slop, intercept form.
#RETURN 2D point of intersection in the format [x-coordinate, y-coordinate].
def intersect(d0, d1):
    a1 = -d0[0]
    a2 = -d1[0]
    b1 = 1
    b2 = 1
    c1 = -d0[1]
    c2 = -d1[1]
    x = ((b1*c2)-(b2*c1))/((a1*b2)-(a2*b1))
    y = ((c1*a2)-(c2*a1))/((a1*b2)-(a2*b1))
    return round(x, 2), round(y, 2)


###########################################################################
# Problem 4
###########################################################################
#INPUT list of numbers
#RETURN dictionary of relative frequency of members in the list
def make_prob(xlst):
    diction = {}
    for i in xlst:
        if i in diction:
            diction[i] +=1
        else:
            diction[i] =1
    for i in diction:
        diction[i] = round((diction[i] / len(xlst)), 2)
        
    return diction



    

###########################################################################
# Problem 5
###########################################################################
#INPUT list of numbers
#RETURN entropy of probability function
#clueless on this one too.
def entropy(lst):
    entr = 0
    i = 0
    for i in lst:
        entr = 1
    return entr



###########################################################################
# Problem 6
###########################################################################
#INPUT List of numbers
#RETURN mean
def mean(lst):
    return round(sum(lst)/len(lst), 2)

#INPUT list of numbers
#RETURN variance
def variance(lst):
    x = mean(lst)
    a = 0
    for i in lst:
        a = a + ((i - x)**2)
        
        
    return round( 1/(len(lst))* a, 2)


#INPUT list of numbers
#RETURN standard deviation (sqrt of variance)
def std(lst):
    x = variance(lst)
    return round(x**(1/2), 2)


#INPUT list of numbers
#RETURN list of mean centered numbers 
def mean_centered(lst):
    newlst = []
    for i in lst:
        newlst.append(((i - mean(lst)), 2))
    return newlst



###########################################################################
# Problem 7
###########################################################################
#INPUT list of numbers and option 0, 1
#RETURN absolutest greatest difference if option = 1, and smallest if option = 0
def blist(lst):
    one = 0
    zero = 0 
    for i in lst[0]:
        if lst[1] == 1:
            a = max(lst[0]) - min(lst[0])
            return a
            #I am confused on how to subtract two values inside the list without manually typing it out like I did below. 
        else:
            newlst = (abs(lst[0][0]-lst[0][1]),abs(lst[0][0]-lst[0][2]),abs(lst[0][0]-lst[0][3]),abs(lst[0][1]-lst[0][2]),abs(lst[0][1]-lst[0][3]),abs(lst[0][2]-lst[0][3]))
            return min(newlst)
          


###########################################################################
# Problem 8
###########################################################################
#INPUT lists of data logs [name,[s1,t1],[s2,t2],...]
#RETURN the name and most mileage
def f_(xlst):
    m = 0
    X = 167.5
    Y = 55
    Z = 20
    A = 60
    if X >= most:
        m = X
        if Y >= m:
            m = Y
            if Z >= m:
                m = Z
                if A >= m:
                    m = A
    return ('X', m)


if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    If you uncomment the following print statements for testing
    then please comment them back before submitting your final version.

    You are encouraged to do some of your own testing by
    trying different values as function parameters in the print 
    statements.
    """

    # #problem 1
    #p1 = [[0,1,1,0,0,0,1,1,1,1],[0,0],[1,1,0,1],[1,1,0,1,1,1,1],
        #[1,1,1,1,1,1,1,1,1,1,1], [0,0,1,1,1,1,0,0]]
    #for x in p1:
        #print(f"{x}  {ls(x)}")

    # #problem 2
    #people0 = [[0,1,1],[1,0,0],[1,1,1]]
    #print(match(people0))
    #print(best_match(match(people0)))

    #people1 = [[0,1,1,0,0,0,1],
                #[1,1,0,1,1,1,0],
                #[1,0,1,1,0,1,1],
                #[1,0,0,1,1,0,0],
                #[1,1,1,0,0,1,0]]
    #print(best_match(match(people1)))
    
    #v0,v1 = (2,3,-1), (1,-3,5)
    #print(f"122 deg = {angle(v0,v1)}") #122

    #v0,v1 = (3,4,-1),(2,-1,1)
    #print(f"85.41 deg = {angle(v0,v1)}") #85.41

    #v0,v1 = (5,-1,1),(1,1,-1)
    #print(f"70.53 deg = {angle(v0,v1)}") #70.53


    # #problem 3
    #l0 = (2,3)
    #l1 = (-1/2,2)
    #print(intersect(l0,l1)) #-2/5,11/5
    #print(intersect((1,4),(-1/2,1/2)))
 
    # #problem 4
    #p4 = [[1,1,0,0],[1,2,3,1,1,2,1],['a','a','b']]

    #for d in p4:
        #print(f"{d} {make_prob(d)}")
    
    # #problem 5
    #p5 = [[1,1,0,0],[1,2,3,1,1,2,1],['a','a','b']]
    #for d in p5:
        #print(f"{entropy(d)}")

    # #problem 6
    p6 = [1,3,3,2,9,10]
    #print(f"mean {mean(p6)}")
    #print(f"variance {variance(p6)}")
    #print(f"std {std(p6)}")
    print(f"mean centered {mean(mean_centered(p6))}")

    # # problem 7
    #p7 = [[[6,2,1,100],1],[[6,2,1,100],0],[[0,0,10,10],1],
    #[[1,2,1,-4],0],[[1,2,1,-4],1],[[0,0,10,10],0]]
    #for d in p7:
        #print(f"{d} {blist(d)}")

    # #problem 8
    # truck_d = [['X', [ 55,[0,60]],[15,[2.5]],[75,[.2,48]]],
    #        ['Y', [55,[0,60]]],
    #        ['Z', [10,[1]],[10,[1]]],
    #        ['A', [30,[2]]]]
    # print(f"{f_(truck_d)}")