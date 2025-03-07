import random

print("Welcome to Dice Simulator")
userInput = 'y'

while userInput == 'y':
    number = random.randint(1, 6)
    if number == 1:
        print("[----------]")
        print("[          ]")
        print("[     0    ]")
        print("[          ]")
        print("[----------]")

    if number == 2:
        print("[----------]")
        print("[          ]")
        print("[   0   0  ]")
        print("[          ]")
        print("[----------]")

    if number == 3:
        print("[----------]")
        print("[     0    ]")
        print("[     0    ]")
        print("[     0    ]")
        print("[----------]")

    if number == 4:
        print("[----------]")
        print("[  0     0 ]")
        print("[          ]")
        print("[  0     0 ]")
        print("[----------]")

    if number == 5:
        print("[----------]")
        print("[  0     0 ]")
        print("[     0    ]")
        print("[  0     0 ]")
        print("[----------]")

    if number == 6:
        print("[----------]")
        print("[  0    0  ]")
        print("[  0    0  ]")
        print("[  0    0  ]")
        print("[----------]")
    userInput = input("Type 'y' to roll again: ")

    if userInput != 'y':
        print("Thanks for playing our game.")