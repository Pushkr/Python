# Create a program that asks the user to enter their name and their age. Print out a message addressed to them 
# that tells them the year that they will turn 100 years old.
# Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the 
# previous message.  
# Print out that many copies of the previous message on separate lines.  

from datetime import timedelta, datetime

name = input("What is your name?")
age = int(input("Hello %s what is your age?" %name))
t_age = timedelta(days=age*365)
BirthYear = datetime.today() - t_age
year100th = BirthYear + timedelta(days=100*365);

msg = "You were born in year %d and you will be 100 year old in year %d \n" %(int(BirthYear.year),int(year100th.year))

print(msg)

rep = int(input("Enter a number:"))

for i in range (0,rep):
    print(msg)
