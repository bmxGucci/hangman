import random

def play_hangman():
    word_list = ["python", "java", "kotlin", "javascript", "ruby"]
    word = random.choice(word_list)
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    letters_guessed = set()
    tries = 6

    print("Hangman Game")
    while len(word_letters) > 0 and tries > 0:
        print("You have", tries, "tries left.")
        print("Available letters:", "".join(alphabet - letters_guessed))
        guess = input("Guess a letter: ").lower()
        if guess in word_letters:
            letters_guessed.add(guess)
            word_letters.discard(guess)
        else:
            tries -= 1
            print("Incorrect.")

        word_as_list = [letter if letter in letters_guessed else "_" for letter in word]
        print(" ".join(word_as_list))

    if tries == 0:
        print("You lost! The word was", word)
    else:
        print("You won! The word was", word)

if __name__ == '__main__':
    play_hangman()
