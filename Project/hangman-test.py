import random
from hangman import check_guess, make_word
import pytest

def test_check_guess():
    # Test case 1: Correct guess with all letters in the right position
    guess = "cat"
    word = "cat"
    hint = check_guess(guess, word)
    assert hint == "CAT"

    # Test case 2: Correct guess with letters in the wrong position
    guess = "car"
    word = "cat"
    hint = check_guess(guess, word)
    assert hint == "CA_"

    # Test case 3: Incorrect guess
    guess = "dog"
    word = "cat"
    hint = check_guess(guess, word)
    assert hint == "___"

def test_make_word():
    # Test that make_word returns a word from the list
    words = [
        "absence", "account", "accident", "beneath", "bend", "benefit", "biology", "bitter", "candidate",
        "campaign", "camera", "capacity", "capture", "deaf", "daughter", "deal", "decorate", "dialogue",
        "economy", "finance", "educate", "efficient", "supportive", "elderly", "flight", "folk", "flame",
        "frustration", "garbage", "gather", "gentle", "global", "hilarious", "intelligence", "jazz", "knife",
        "longevity", "monument", "nonsense", "nobody", "turmeric", "utilize", "sashimi", "reconfigure",
        "wheat", "yellowish", "zone"
    ]
    random.seed(42)  # Set seed for consistent testing
    word = make_word()
    assert word in words

    # Test that make_word returns a different word on subsequent calls
    random.seed(43)
    new_word = make_word()
    assert new_word != word

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])