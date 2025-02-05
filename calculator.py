import re

def add(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    print(f"Answer: {num1} + {num2} = {num1+num2}")

def sub(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    print(f"Answer: {num1} - {num2} = {num1-num2}")

def mult(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    print(f"Answer: {num1} x {num2} = {num1*num2}")

def div(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    ans = num1 / num2
    print(f"Answer: {num1} / {num2} = {ans:.2f}")

while 1:
    userInput = input("Input: ")
    userSplit = re.split("\s",userInput)

    if "+" in userSplit:
        add(userSplit[0],userSplit[-1])
    elif "-" in userSplit:
        sub(userSplit[0],userSplit[-1])
    elif "*" in userSplit:
        mult(userSplit[0], userSplit[-1])
    elif "/" in userSplit:
        div(userSplit[0], userSplit[-1])
    else:
        print("The calculator is exiting...")
        break