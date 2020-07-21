import getpass
import re

def guess_function(word, hangword):

    hangman = 'HANGMAN'
    letters_used = []
    turns = 0

    print(hangman)
    print(f"The letters used are {', '.join(letters_used)}")
    print("")

    playing = True

    while playing:

        if hangword.split("/") == word.split():
            print(f"\nCongratulations! You guessed the phrase '{word}' correctly in just {turns} turns!\n")
            break
        elif hangman == "":
            print(f"\nUh-oh! You ran out of chances :( The phrase was '{word}'\n")
            break

        turns += 1

        while True:
            guess = input("Guess any alphabet: ").lower()
            if not guess:
                continue
            elif guess == word:
                print(f"Congratulations you guessed the phrase {word} correctly in just {turns} turns!")
                playing = False
            elif len(guess) > 1:
                print("Sorry, you may only enter 1 letter")
            elif guess in letters_used:
                print("Sorry, you have already used this letter")
            else:
                break

        if not playing:
            break

        letters_used.append(guess)
        if guess in word:
            print(f"\nCorrect! {guess} is there in the word!")
            hanglist = list(hangword)
            for i in re.finditer(guess, word):
                hanglist[i.start()] = guess
            hangword = "".join(hanglist)
        else:
            print(f"\nUh-oh! {guess} isn't in this word :(")
            hangman = hangman[:-1]


        print(hangword)
        print(hangman)
        print(f"The letters used are {', '.join(letters_used)}")
        print("")


print('Welcome to HANGMAN'.center(50,'-'))
print("created by Pratham Mehta".center(50))
print("\nThe rules for this game are pretty simple and the rules are as follows:")
print("\t- Player 1 enters a phrase that they want the other player to guess (text is hidden as typed)")
print("\t- The locations of the vowels are highlighted with a '#'")
print("\t- Player 2 keeps guessing alphabets, and every time an incorrect letter is entered, an alphabet will be slashed from 'HANGMAN' as shown on the screen")
print("The game ends either when Player 2 guesses the phrase correctly (P2 wins) or when all letters of HANGMAN are slashed (P1 wins)")
print("Hit ENTER to start playing! \n")
print("_"*50+"\n")

input()

secret_word = getpass.getpass(prompt="What's the secret phrase?: ").lower()

hangman_word = ""

for l in secret_word:
    if l == " ":
        hangman_word += "/"
    elif l.lower() not in "bcdfghjklmnpqrstvwxyz":
        if l.lower() in 'aeiou':
            hangman_word += '#'
        else:
            hangman_word += l
    else:
        hangman_word += '_'

print(hangman_word)

guess_function(secret_word, hangman_word)

