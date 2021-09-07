import random

#  Tool Commands
def UserInput () :
    UserIn = int(input("Enter your 4 digit guess: "))
    return UserIn

def ListToString(s):
    str1 = " "
    return (str1.join(s))

# Inialize Variables
MasterCode = list(str(random.randrange(1000,9999)))
x = 1

# Inital User Interface
print("You have 10 guesses to find the correct 4 digit number.")
print("A 'Y' indicates that the digit is correct, a 'N' indicates that the digit is incorrect")
print("-------------------------------------------------------")

# Command Loop with 10 cycles
while x < 11:
    # Empty list to store output correct/incorrect answers
    Answer = []
    # Prompting the user for a guess
    UserGuess = list(str(UserInput()))
    if (len(UserGuess)) != 4:
        print("Your guess must be exactly 4 digits")
        pass
    else:
        # Loop to check if the answer is correct and adding that to the Answer list
        for i in range(0,4):
            if (UserGuess[i] == MasterCode[i]):
                Answer.append("Y")
            else:
                Answer.append("N")
        print(ListToString(Answer))
        print("You now have", 10-x, "guesses left.")
        print("-----------------------------------")
    # Checking Win condition
    if (ListToString(Answer).replace(" ","") == "YYYY"):
        print("You Win!!")
        break
    else:
        x+=1
        if (x == 10):
            print("You Loose!")
            break
