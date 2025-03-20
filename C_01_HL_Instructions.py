# functions go here


def yes_no(question):
    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes/no")


def instructions():
    print('''
    
*** Instructions ***

To begin, choose the number of rounds and either customise
 the game parameters or go with the default game (where the
 secret number will be between 1 and 100).
 
 Then choose how many rounds you'd like to play <enter> for
 infinite mode.
 
 Your goal is to try guess the secret number without
 running out of guesses.
 
 Good luck.
 
   ''')

# main routine
print()
print("⬆️⬆️⬆️ Welcome to the higher lower Game 🔽🔽🔽")
print()

# loop fpr testing purposes

want_instructions = yes_no("Do you want to read the instructions? ")

# checks user enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print("program continues")
