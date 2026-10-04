import random
random_number = random.randint(1,1000)
guess_count = 0

# Imports random module so we can later use "randint" function. 
# Creates a variable, "random_number", and sets it equal to a random integer between 1 and 1000.
# Creates a variable, "guess_count", and sets it equal to 0


def show_intro():
    print("Welcome to the Number Guesser Game!")
    print("Please input a number between 1 and 1000.")
    print("Type 'bye' or 'exit' to quit the game.")

# Created a function "show_intro()" to consolidate print statements before while loop to make code more readable.



def quit_game():
    print("Thanks for playing!")

# Created a function called "quit_game()" to make code more condensed and readable. 

show_intro()

# Called "show_intro()" function before while loop to ensure user instructions were only printed before user makes first guess for first time.

while True:
    response=input("Enter a number or 'bye' or 'exit' to quit game:").strip().lower()
    if response in ("exit","bye"):
        quit_game()
        break

# Allows user to input either a number or 'bye' or 'exit' to quit game.
# In case, bye or exit is inputted with varying capitalization or with spaces before/after, .strip() and .lower() removes spaces and lowercases string.
# Created a tuple that checks if response is equal to "exit" or "bye".
# If response is equal to either string, quit_game() is called, which prints "Thanks for playing!".
# Break exits loop
    
    try:
        guess=int(response)
        guess_count += 1
    except ValueError:
        print ("Please enter a valid number.")
        continue

# The while loop then creates a variable called, "guess", which is equal to the integer conversion of response string.
# If the response string successfully converts to an integer, "guess_count" variable is increased by 1 and takes new value.
# If there is an error when interpreter attempts to convert response into an integer, "Please enter a valid number." is printed.
# CONTINUE tells the interpreter to go back to the beginning of loop.   
    
    if guess > random_number:
     print("Too High! Try Again.")
    elif guess < random_number:
     print("Too Low! Try Again.")
    else:
     print("Congratulations! You guessed the right number!")
     print("You took", guess_count, "guess(es).")
     guess_count = 0 
     random_number = random.randint(1,1000)
     continue

# Used if-else statements to compare "guess" variable to "random_number" variable and print appropriate hint/response.
# Else statement includes:
# Print statements for Congrats message and Number of guesses it took to guess right number.
# Automatically resets "guess_count" variable back to 0 and picks another number for "random_number" variable, for next iteration of while loop
# CONTINUE says do it all over again from the top. 



