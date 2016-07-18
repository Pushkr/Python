# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the
# first and last elements of the given list. For practice, write this code inside a function.

import random


def GetEndsOfList(ListA):
    try:
        if len(ListA) < 2:
            return ListA[0], 'Not Available'
        else:
            ListB = [x for x in ListA if x==ListA[0] or x==ListA[len(ListA) - 1]]
            return ListB
    except:
            print("Passed argument not a list \n")




#print(GetEndsOfList(10))

List = GetEndsOfList(random.sample(range(0,100),20))
print("First Element of List : ",List[0])
print("Last Element of List  : ",List[1])
