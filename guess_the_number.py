import random

print("Welcome to Guess The Number")
wins = 0
computer_number = random.randint(1, 100)

while True:
    tries = 5

    while True:
        player_number = input("Guess the number: ")
        if not player_number.isdigit():
            print("Invalid input")
            continue

        if int(player_number) == computer_number:
            print("You guessed it!")
            print("Moving to next level!")
            wins += 1
            break

        elif tries == 1:
            print("Nice try!")
            break

        elif int(player_number) > computer_number:
            tries -= 1
            print("Too high")

        elif int(player_number) < computer_number:
            tries -= 1
            print("Too low")

    play_again = input("Do you want to play again? ")

    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break

    if wins > 0:
        computer_number = random.randint(1, 200)
        print("Level 2! Guess between 1 and 200.")
    else:
        computer_number = random.randint(1, 100)


