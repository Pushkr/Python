import random
ListA=['rock','paper','scissor']
play_again = 'y'
while play_again == 'y' :
        user_choice = ''
        user_choice=input("Lets play rock paper scissors! your turn, chose:").lower()
        computer_choice=random.choice(ListA)
        print("** computer selects %s**" %computer_choice)
        if user_choice==computer_choice:
            print("Draw!")
        elif user_choice=='rock' and computer_choice=='paper':
            print("paper beats rock, I win, you lose!")
        elif user_choice=='rock' and computer_choice=='scissor':
            print("rock beats scissors, you win!")
        elif user_choice=='paper' and computer_choice=='scissor':
            print("Scissor beats paper, I win, you lose!")
        elif user_choice=='paper' and computer_choice=='rock':
            print("rock beats paper, I win!")
        elif user_choice=='scissor' and computer_choice=='rock':
            print("rock beats scissors, I win, you lose!")
        elif user_choice=='scissor' and computer_choice=='paper':
            print("Scissor beats paper, you win!")
        else:
            print("select between rock, paper and scissor only, dummy!")

        play_again=input("play again?(y/n)").lower()
