
def zero_every_other(xlist):
    """
    Function to zero out every other element of a list,
    starting from the first element.

    Example:
    >>> zero_every_other([1, 2, 3, 4, 5])
    [0, 2, 0, 4, 0]
    """
    for i in range(len(xlist)):
        if i % 2 == 0:
            xlist[i] = 0
    return xlist

def zero_every_other_comp(xlist):
    """
    Rewrite zero_every_other using a list comprehension
    """
    pass

def tempreture(temp_dict):
    """
    given a dictionary of Tempretures of the days at noon as an input. for those above 60 return hot for those less than or equal to 60 returns cold
    """
    pass


if __name__ == "__main__":
    print("****************************")
    print("* TESTING ZERO_EVERY_OTHER *")
    print("****************************")
    tests = [([1, 2, 3, 4, 5], [0, 2, 0, 4, 0])]

    for xlist, expected in tests:
        print("input list:", xlist, "\n")
        print("every_other:", zero_every_other(xlist))
        print("list comp:", zero_every_other_comp(xlist))
        print("expected:", expected)

    my_dict = {'Monday': 38, 'Tuesday': 70, 'Wednesday': 57, 'Thursday': 93}
    print(tempreture(my_dict))
