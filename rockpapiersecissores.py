import random
print("welcome to rock paper scissors")
ROCK = "r"
PAPER = "p"
SCISSORS = "s"
# using a dictionary to map choices to emojis
emoji = {ROCK: '🪨', PAPER: '📄', SCISSORS: '✂️'}
# choices = ("r", "p", "s") # this tuple but we could use dry principle to avoid repeating the choices in multiple places in the code.
# with this way we have applied the DRY principle and we can easily change the choices in one place if needed, and it also makes the code more readable by using the emoji keys directly.
choices = tuple(emoji.keys())


def getting_user_input():
    while True:
        user = input("choose r/p/s: ").lower()
        if user not in choices:
            print("invalid input. please choose r, p, or s.")
            continue
        return user


def winning_conditions(user, computer):
    if user == computer:
        return "tie"
    elif user == ROCK and computer == SCISSORS or user == PAPER and computer == ROCK or user == SCISSORS and computer == PAPER:
        return "win"
    else:
        return "lose"


def print_choices(user, computer):
    print(" you chose", emoji[user], "and the computer chose", emoji[computer])


def play_again():
    while True:
        play_again = input("play again? y/n: ").lower()
        if play_again == "y":
            return True
        elif play_again == "n":
            print("thanks for playing!")
            return False
        else:
            print("invalid input. please enter y or n.")


def play_game():
    while True:
        computer = random.choice(choices)
        user = getting_user_input()
        result = winning_conditions(user, computer)

        if result == "tie":
            print("tie")
        elif result == "win":
            print_choices(user, computer)
            print("you win")
        else:
            print_choices(user, computer)
            print("you lose")

        if not play_again():
            break


play_game()
