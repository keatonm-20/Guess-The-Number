import random

while True:
    random_number = random.randint(1, 10)
    player_number = int(input("Enter Number: "))

    while True:
        if random_number == player_number:
            print("Correct!")
            break
        else:
            print("Try Again: ")
            player_number = int(input("Enter Number: "))

