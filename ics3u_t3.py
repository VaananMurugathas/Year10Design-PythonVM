# Here is a program to show how to use "if - elif - else"
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Mr. Jugoon
# Upper Canada College

# Put down some options for the user to choose from...
import random

print("1. Weather")
print("2. Classes")
print("3. After school")
print(" ")
print("Choose one of the options above")

mood = int(input("What do you want to know? \n"))

if mood == 1:
    print("Today's weather is sunny with a high probability of rain")
elif mood == 2:
    print ("Today's day is " + str(random.randint(1,8)))
elif mood == 3:
    print ("After school you have soccer today")
else:
    print ("This is not a valid choice")
    print ("Hope you have a great day anyway!")


# This is a way to gracefully exit the program
input("Press ENTER to quit the program")
