#FizzBuzz 4 and 6

import time
# Checking Commands
def Check6 (num):
    if (num%6) == 0:
        return True
    else:
        return False

def Check4 (num):
    if (num%4) == 0:
        return True
    else:
        return False

# User Interface
Lenght = int(input("How long do you want to FizzBuzz {Upper limit}: "))
print("-----------------------------------")

# Command Loop
for i in range (1,Lenght+1):
    if (Check6(i) and Check4(i)):
        print("FizzBuzz")
        pass
    elif (Check6(i)):
            print("Buzz")
            pass
    elif (Check4(i)):
            print("Fizz")
            pass
    else:
        print(i)


print("----------------------")
print("FizzBuzz Loop Complete")
time.sleep(20)
