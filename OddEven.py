# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


num = int(input("Enter a number:"))
check = int(input("Enter 2nd number:"))

if num%2 == 0:
    print("Number %d is even" %num)
else:
    print("Number %d is odd" %num)

if num%4==0 :
    print("Also, number %d is divisible by 4" %num)

if num%check==0:
    print("and number %d is also divisible by %d" %(num,check))
else:
    print("but number %d is not divisible by %d" %(num,check))
