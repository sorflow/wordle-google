import random
import sys

def main():
    # Get a random word.
    answer = getRandomWord()
    attempts = 0
    correct = False
    guessColors = []
    while attempts < 6 and not correct:
        guess = input("Enter a 5 letter guess?\n")
        if len(guess) != 5:
            print("Please enter a 5 letter guess.")
        else:
            guessColors = [letterColor(i, guess, answer) for i in range(len(guess))]
            printGuessColors(guess, answer, guessColors)
            attempts += 1
            if all(color == "Green" for color in guessColors):
                correct = True
                print("You Won! That took " + str(attempts) + " guess(es).")
    if not correct:
        print("You lost. The answer was", answer + ".")


def printGuessColors(guess, answer, guessColors):
    for i in range(len(guess)):
        if i < len(answer):
            color = guessColors[i]
            print(guess[i] + " - " + color)
        else:
            print(guess[i] + " - Out of range")

def letterColor(index, guess, answer):
    if guess[index] == answer[index]:
        return "Green"
    elif guess[index] in answer:
        return "Yellow"
    else:
        return "Red"

def getRandomWord():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        words = [word.strip() for word in file.readlines()]
        return random.choice(words)

main()
