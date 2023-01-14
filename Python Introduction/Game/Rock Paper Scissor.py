# Rock Paper Scissor Game

from random import choice


def is_win(player, opponent):

    if (
        (player == "p" and opponent == "r")
        or (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
    ):

        return True


def play():

    user = input("What's your choice ? 'r' for Rock, 'p' for Paper , 's' for Scissor\n")

    computer = choice(["r", "p", "s"])  # ? random.choice()

    print("Computer choose ", computer)

    if user == computer:

        return "It's a tie"

    if is_win(user, computer):

        return "You win"

    return "You lose"


print(play())
