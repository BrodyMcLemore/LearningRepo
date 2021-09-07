# Importing the needed Librs
import random
import time

# Creating the global Vars
Final_Num = random.randint(1,100)
counter =  5 # This controls the difficulty

# Setting the inital User interactions
print("Try and guess the Final Number between 1 and 100.")
print("-----------------------------------")
print("You have", counter, "guesses left.")

# The running loop
while True:
   User_Ans = int(input("What is your guess? "))
   if  counter == 0:
        print("Oh you ran out of guesses, GAME OVER")
        print("The number was",Final_Num)
        time.sleep(20)
        break
   else:
        if  User_Ans == Final_Num:
            print("You guessed the Final Answer!!")
            break
        elif User_Ans > Final_Num:
            counter -= 1
            print("Your guess is larger than the answer. Try agian you have", counter, "guesses left.")
        elif User_Ans < Final_Num:
            counter -= 1
            print("Your guess is smaller than the answer. Try agian you have", counter, "guesses left.")
