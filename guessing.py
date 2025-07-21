secret_word = "lion"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while not(out_of_guesses) and guess!=secret_word:
    if guess_count < guess_limit:
        guess = input("Enter guess : ")
        
        if guess == secret_word:
            print("you win")
            break
            
        else:
            print("That's not the correct word")
            guess_count += 1
            
    else:
        print("Sorry you are out of guesses")
        out_of_guesses = True
