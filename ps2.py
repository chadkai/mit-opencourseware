# Problem Set 2, hangman.py
# Name: Cai Si Kai
# Collaborators: - 
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    word_list = []
    for i in list(secret_word):
        if i in letters_guessed:
            word_list.append(1)
        else:
            word_list.append(0)
    if word_list.count(1) == len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    guessed_list = []
    for i in list(secret_word):
        if i in letters_guessed:
            guessed_list.append(i)
        else:
            guessed_list.append("_")
    return (' '.join(guessed_list))


def get_available_letters(letters_guessed):
    left_list = list(string.ascii_lowercase)
    for i in left_list:
        if i in letters_guessed:
            left_list.remove(i)
    return (''.join(left_list))


def hangman(secret_word):
    # Introducing player to the game
    print("Welcome to Hangman!")
    print("You have a total of 6 guesses.")
    print("Number of letters in the secret word: ", len(secret_word))

    # Vowel list
    vowel_list = ['a', 'e', 'i', 'o', 'u']

    # The user should start with 6 guesses and 3 warnings
    guesses = 6
    warnings = 3

    # Initializing a list
    letters_guessed = []

    while True:
        if is_word_guessed(secret_word, letters_guessed) == False:
            print("Available letters: ", get_available_letters(letters_guessed))
            guess_letter = str(input("Please guess a letter: "))

            # Breaking the loop when warnings are exceeded
            if warnings == 0:
                print("You exceeded 3 warnings. You lost the game! \nThe secret word is: ", secret_word)
                break

            # Breaking the loop when guesses are exceeded
            elif guesses == 0:
                print("You exceeded 6 guesses. You lost the game! \nThe secret word is: ", secret_word)
                break

            # Checking if input letter is valid or not
            elif guess_letter.isalpha() == False:
                warnings -= 1
                print("Oops! That is not a valid letter. You have {} warnings left.".format(warnings))

            else:
                # Process if guessed letter is indeed in the secret word
                if guess_letter in secret_word:
                    letters_guessed.append(guess_letter)
                    # Checking if the letters are repeated
                    if letters_guessed.count(guess_letter) > 1:
                        warnings -= 1
                        print("Oops! You've already guessed the letter: ", get_guessed_word(secret_word, letters_guessed))
                        print("You have {} warnings left.".format(warnings))
                    # Checking if the letters are in the word
                    else:
                        print("That letter is indeed in the word: ", get_guessed_word(secret_word, letters_guessed))
                        print("You still have {} guesses left.".format(guesses))

                # Process if guessed letter is not in the secret word
                else:
                    letters_guessed.append(guess_letter)
                    if guess_letter in vowel_list:
                        guesses -= 2
                    else:
                        guesses -= 1
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                    print("You have {} guesses left.".format(guesses))

            # Lines to demarcate
            print("-----------")

        else:
            print("Congratulations, you guessed the word correctly!")
            break


def match_with_gaps(my_word, other_word):
    check_list = []
    my_word_list = my_word.split(' ')
    other_word_list = list(other_word)
    if len(my_word_list) == len(other_word_list):
        for i in range(0, len(my_word_list)):
            if my_word_list[i] == other_word_list[i]:
                check_list.append(1)
            elif my_word_list[i] == '_':
                check_list.append(1)
            else:
                check_list.append(0)
    else:
        return False
    if 0 in check_list:
        return False
    else:
        return True


def show_possible_matches(my_word):
    check_list2 = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            check_list2.append(word)
    return ' '.join(check_list2)

def hangman_with_hints(secret_word):
    # Introducing player to the game
    print("Welcome to Hangman!")
    print("You have a total of 6 guesses.")
    print("Number of letters in the secret word: ", len(secret_word))

    # Vowel list
    vowel_list = ['a', 'e', 'i', 'o', 'u']

    # The user should start with 6 guesses and 3 warnings
    guesses = 6
    warnings = 3

    # Initializing a list
    letters_guessed = []

    while True:
        if is_word_guessed(secret_word, letters_guessed) == False:
            print("Available letters: ", get_available_letters(letters_guessed))
            guess_letter = str(input("Please guess a letter: "))

            if guess_letter == '*':
                print("Possible word matches are: \n", show_possible_matches(get_guessed_word(secret_word, letters_guessed)))

            # Checking if input letter is valid or not
            elif guess_letter.isalpha() == False:
                warnings -= 1
                print("Oops! That is not a valid letter. You have {} warnings left.".format(warnings))

            else:
                # Process if guessed letter is indeed in the secret word
                if guess_letter in secret_word:
                    letters_guessed.append(guess_letter)
                    # Checking if the letters are repeated
                    if letters_guessed.count(guess_letter) > 1:
                        warnings -= 1
                        print("Oops! You've already guessed the letter: ", get_guessed_word(secret_word, letters_guessed))
                        print("You have {} warnings left.".format(warnings))
                    # Checking if the letters are in the word
                    else:
                        print("That letter is indeed in the word: ", get_guessed_word(secret_word, letters_guessed))
                        print("You still have {} guesses left.".format(guesses))

                # Process if guessed letter is not in the secret word
                else:
                    letters_guessed.append(guess_letter)
                    if guess_letter in vowel_list:
                        guesses -= 2
                    else:
                        guesses -= 1
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                    print("You have {} guesses left.".format(guesses))

            # Breaking the loop when warnings are exceeded
            if warnings == 0:
                print("You exceeded 3 warnings. You lost the game! \nThe secret word is: ", secret_word)
                break

            # Breaking the loop when guesses are exceeded
            elif guesses == 0:
                print("You exceeded 6 guesses. You lost the game! \nThe secret word is: ", secret_word)
                break
            # Lines to demarcate each guess
            print("-----------")

        else:
            print("Congratulations, you guessed the word correctly!")
            break




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
