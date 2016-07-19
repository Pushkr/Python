# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the
# user the same string, except with the words in backwards order.

#Reversing a string using string manupulation

def ReverseIt(user_input):
    output = ''
    oplist = user_input.split()
    for i in range(len(oplist)-1, -1, -1):
        output = output + oplist[i] + ' '
    return output

#Reversing a string using split ,join functions and List comprehension .
def ReversetItByJoin(user_input):
   output1 = [x for x in user_input.split(' ')[::-1]]
   output = ' '.join(output1)
   return output

#Reversing a string using reversed, split and join functions.
def ReverseitByfunction(user_input):
   oplist = reversed(user_input.split(' '))
   return ' '.join(oplist)


str = (input("say something:"))

print(ReverseIt(str))
print(ReversetItByJoin(str))
print(ReverseitByfunction(str))
