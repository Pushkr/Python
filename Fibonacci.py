''''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this
opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers
in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in
the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''


def Recursive(i,ListA,counter) :
    try:
         ListA.append(ListA[i+1] + ListA[i])
         i +=1
         if len(ListA) == counter:
            print(ListA)
            return
         else:
            Recursive(i,ListA,counter)
    except:
        print("Error encountered while generating series")


ListA=[]
# while True:
try:
        counter = int(input("How many fobinacci numbers to generate?"))
        ListA.append(int(input("Enter first number:")))
        ListA.append(int(input("Enter second number:")))
        # All Ok then Call function
        Recursive(0,ListA,counter)
except ValueError:
        print("Invalid input, please enter integers only")
