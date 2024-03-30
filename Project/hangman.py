import random

def main():
    # Instructions for the game
    instructions = """
Instructions:
The computer has chosen a secret word.
You need to guess the word by entering letters one at a time.
Each time you guess a letter, you will be given a hint.
The hint will show you if the letter you guessed is correct and in the right position (capitalized),
or if it's correct but in the wrong position (lowercase), or if it's not in the word (underscore).
Keep guessing letters until you figure out the entire word.
Once you guess the word correctly, you win the game!
The game will tell you how many guesses it took you to win.
    """
    print(instructions)
    
    # Generate the secret word
    word = make_word()
    
    # Display the word and initial hint
    print(word)
    hint = "_ " * len(word)
    print(f"The word has {len(word)} letters.")
    print(f"The hint is {hint}\n")

    counter = 0
    while True:
        # Player makes a guess
        guess = input("What's your guess? ")
        counter += 1

        if len(guess) != len(word):
            # Check if the guess has the correct length
            print(f"The guess must have {len(word)} letters.")
        else:
            # Check the guess and generate a hint
            hint = check_guess(guess, word)
            print(f"The hint is {hint}")

        if guess.lower() == word:
            # Check if the guess is correct
            print("That's correct!")
            break

    if counter > 1:
        # Display the number of guesses
        print(f"It took you {counter} guesses.")
    else:
        print(f"It took you {counter} guess.")

def check_guess(guess, word):
    # Check the correctness of the guessed word and generate a hint
    hint = ""
    for index, letter in enumerate(guess):
        if letter == word[index]:
            hint += letter.upper()
        elif letter in word:
            hint += letter.lower()
        else:
            hint += "_"
    return hint

def make_word():
    # Select a random word from a predefined list
    words = [
        "absence", "account", "accident", "beneath", "bend", "benefit", "biology", "bitter", "candidate",
        "campaign", "camera", "capacity", "capture", "deaf", "daughter", "deal", "decorate", "dialogue",
        "economy", "finance", "educate", "efficient", "supportive", "elderly", "flight", "folk", "flame",
        "frustration", "garbage", "gather", "gentle", "global", "hilarious", "intelligence", "jazz", "knife",
        "longevity", "monument", "nonsense", "nobody", "turmeric", "utilize", "sashimi", "reconfigure",
        "wheat", "yellowish", "zone"
    ]
    return random.choice(words)

if __name__ == "__main__":
    main()
