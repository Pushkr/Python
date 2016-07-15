# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

#Make a dictionary 
Vlist = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

play_again = 'y'
count = 0

#Machine makes a choice
computer_choice=random.choice(range(1,10))

while play_again != 'exit':
    user_choice=''
    try:
        user_choice=int(input("Guess a number (between 1 to 9):"))
        count += 1
        Vlist[user_choice]+=1
        if user_choice < computer_choice:
            print("You guessed it too low")
        elif user_choice > computer_choice:
            print("You guessed it too high")
        elif user_choice == computer_choice:
            print("Bingo! you guessed it right")
            print("and it only took you %d attempts to get it right!" %count)

        play_again = input("Guess again(type y) or exit (type exit)")

    except ValueError:
        print("Enter a valid guess")


#Print statistics
for i in Vlist:
    print("You guessed number '%s'  %s times" %(i,Vlist[i]))
