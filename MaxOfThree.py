#Max Of Three  
#Exercise
#Implement a function that takes as input three variables, and returns the largest of the three.
#Do this without using the Python max() function! 
#The goal of this exercise is to think about some internals that Python normally 
#takes care of for us. All you need is some variables and if statements!


def MaxOfThree(num1,num2,num3):
    if num1 == num2 & num2 == num3:
        print("All numbers are equal")
    elif (num1 > num2) & (num1 > num3):
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3


x = MaxOfThree(4,3,1)
print(x)
