# ----------------------------------------------------------------------
# This is the file number_guesser.py
#
# The intent is to give you practice writing a complete, interactive
# Python program.
#
# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
#
# Things to do:
#
# Generate a random number between 1 and 1000.
#
# Ask the user to guess the number. In your prompt, let the user know they
# can type 'bye' or 'exit' to quit the program.
#
# If their guess is not made up entirely of digits, print "Please enter a valid
# number" and ask them to guess again.
#
# If the guess is too high, print "Too high!" and continue asking.
#
# If the guess is too low, print "Too low!" and continue asking.
#
# If the guess is correct, print "Congratulations! You guessed the number!" along
# with the number of attempts it took to guess the number. Start over with a new
# random number. Make sure to zero out the number of attempts.
#
# Please note: There are likely to be a number of Python guessing games online,
# and most GenAI systems can probably write this for you. Don’t rely on them,
# as they rob you of a chance to practice your Python skills and they might not
# even be correct. Perhaps, worse, they might not follow the instructions
# exactly as given.
# 
import random
random_number = random.randint(1,1000)
guess_count = 0

def show_intro():
    print("Welcome to the Number Guesser Game!")
    print("Please input a number between 1 and 1000.")
    print("Type 'bye' or 'exit' to quit the game.")

def guess_game():
    show_intro()

def quit_game():
    print("Thanks for playing!")



while True:
    response=input("Enter a number:").strip().lower()
    if response in ("exit","bye"):
        quit_game()
        break
    try:
        guess=int(response)
        guess_count += 1
    except ValueError:
        print ("Please enter a valid number.")
        continue
    if guess > random_number
    print("Too High! Try Again.")
    elif guess < random_number
    print("Too Low! Try Again.")
    else 
    print("Congratulations! You guessed the right number!")
    guess_count_total = guess_count
    print("You took", guess_count_total, "guesses.")
    guess_count = 0 
    random_number = random.randint(1,1000)
    continue



