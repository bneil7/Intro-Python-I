import random

# file i/o functions for historical results


def load_results():
    text_file = open("history.txt", "r")
    history = text_file.read().split(",")
    text_file.close()
    return history


def save_results(w, t, l):
    text_file = open("history.txt", "w")
    history = text_file.write(str(w) + "," + str(t) + "," + str(l))
    text_file.close()


# welcome message
results = load_results()
wins = int(results[0])
ties = int(results[1])
losses = int(results[2])
print("Welcome to Rock, Paper, Scissors!")
print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))
print("Please choose to continue...")


# initialize user, computer choices
computer = random.randint(1, 3)
user = int(input("[1] Rock  [2] Paper  [3] Scissors   [9] Quit\n"))

# gameplay loop
while not user == 9:
    # user chooses Rock
    if user == 1:
        if computer == 1:
            print("Cpu chose Rock... TIE!")
            ties += 1
        elif computer == 2:
            print("Cpu chose Paper... Paper covers Rock, you lose.")
            losses += 1
        else:
            print("Cpu chose Scissors... Rock smashes Scissors, you win!")
            wins += 1

    # user chooses Paper
    elif user == 2:
        if computer == 1:
            print("Cpu chose Rock... Paper covers Rock, you win!")
            wins += 1
        elif computer == 2:
            print("Cpu chose Paper... TIE!")
            ties += 1
        else:
            print("Cpu chose Scissors... Scissors cuts Paper, you lose.")
            losses += 1

    # user chooses Scissors
    elif user == 3:
        if computer == 1:
            print("Cpu chose Rock... Rock smashes Scissors, you lose.")
            losses += 1
        elif computer == 2:
            print("Cpu chose Paper... Scissors cuts Paper, you win!")
            wins += 1
        else:
            print("Cpu chose Scissors... TIE!")
            ties += 1

    else:
        print("Invalid selection. Please try again with 1, 2, or 3.")
    # print updated stats
    print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))

    # prompt user to make another selection
    print("Please choose to continue...")
    # initialize user, computer choices
    computer = random.randint(1, 3)
    user = int(input("[1] Rock  [2] Paper  [3] Scissors   [9] Quit\n"))

# game over, save results
save_results(wins, ties, losses)
