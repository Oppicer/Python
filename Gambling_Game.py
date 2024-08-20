import os
import sys

def restart_program():
    print("Restarting...")
    os.execv(sys.executable, ['python'] + sys.argv)


Question = input("would you like to gamble? yes or no?")
if Question == "yes":
    print("Great! Let's play a game.")
else: print("Alright, let's play another time.")
Question2 = input("how much do you want to bet")
print("You bet", Question2)
print("You lost")
question3 = input("Do you want to play again? yes or no?")
if question3 == "yes":
    restart_program()
else: print("Alright, let's play another time.")