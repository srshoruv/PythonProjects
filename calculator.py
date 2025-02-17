import re
import os

file = open("calc.txt", "a")

def add(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    ans = f"{num1} + {num2} = {num1+num2}\n"
    file.write(ans)
    print(f"Answer: {num1} + {num2} = {num1+num2}")

def sub(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    ans = f"{num1} - {num2} = {num1 - num2}\n"
    file.write(ans)
    print(f"Answer: {num1} - {num2} = {num1-num2}")

def mult(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    ans = f"{num1} x {num2} = {num1 * num2}\n"
    file.write(ans)
    print(f"Answer: {num1} x {num2} = {num1*num2}")

def div(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    if num2 == 0:
        print("Divisor Cannot be Zero!")
        return
    ans = num1 / num2
    fans = f"{num1} / {num2} = {ans:.2f}\n"
    file.write(fans)
    print(f"Answer: {num1} / {num2} = {ans:.2f}")

while 1:
    userInput = input("Type the expression or ('help' to see options): ")
    userSplit = re.split("\s",userInput)

    if "+" in userSplit:
        add(userSplit[0],userSplit[-1])
    elif "-" in userSplit:
        sub(userSplit[0],userSplit[-1])
    elif "*" in userSplit:
        mult(userSplit[0], userSplit[-1])
    elif "/" in userSplit:
        div(userSplit[0], userSplit[-1])
    elif "exit" in userSplit:
        print("The calculator is exiting...")
        break
    elif "history" in userSplit:
        try:
            file = open("calc.txt", "r")
        except FileNotFoundError:
            print("History Not Found!")
        else:
            print(file.read())
            file.close()
    elif "clear" in userSplit:
        try:
            os.remove("calc.txt")
        except FileNotFoundError:
            print("History is already Cleared!")
        else:
            print("Clearing history...")
    elif "help" in userSplit:
        print("'history' to see history.\n'clear' to clear history.\n'Exit' to terminate the program.\n")
    else:
        print("Invalid input!")
