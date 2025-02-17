from random import randint
import os

selectLevel = int(input("Select Level:\n1: Easy (1-10)\n2: Medium (1-50)\n3: Hard (1-100)\nYour Choice: "))
num = 0
attemptLimit = 3
# generating random number
def generate_num():
    global num
    global attemptLimit
    if selectLevel == 1:
        num = randint(1,10)
        print("Guess the number between 1 to 10")
    elif selectLevel == 2:
        num = randint(1, 50)
        attemptLimit = 5
        print("Guess the number between 1 to 50")
    elif selectLevel == 3:
        num = randint(1, 100)
        attemptLimit = 10
        print("Guess the number between 1 to 100")
generate_num()

userInput = int(input("Enter your guess: "))
attempt = 1

while 1:
    # Checking attempts
    if userInput != num and attempt == attemptLimit:
        afterFailing = input(f"You Failed! The answer was {num}. Try again? : ")
        if afterFailing.lower() == "yes":
            generate_num()
            userInput = int(input("Enter your guess: "))
            attempt = 1
        else:
            print("Thanks for playing the game!")
            break

    # Checking answers
    if userInput == num:
        print(f"Congratulations..You've guessed it right in {attempt} attempts!")
        again = input("Do you want to play again? : ")
        if again.lower() == "yes":
            attempt = 0
            generate_num()
            userInput = int(input("Enter your guess: "))
        else:
            print("Thanks for playing the game!")
            break
    elif userInput > num:
        print("Lower!")
        userInput = int(input("Enter your guess: "))
    elif userInput < num:
        print("Higher!")
        userInput = int(input("Enter your guess: "))
    attempt += 1

file = open("score.txt", "w")
file.write(f"You Have used {attempt} attempts to solve!")
file = open("score.txt", "r")
print(file.read())
