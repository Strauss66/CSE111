#Author: Johan Guerrero-Avitias
import random 
def main():
    words = ["apple", "car", "sky"]
    numbers = [16.2, 75.1, 52.3]
    print(numbers)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers,3)
    print(numbers)

    append_random_words(words)
    print(words)

def append_random_numbers(number_list, quantity=1):
    for _ in range(quantity):
        random_num = random.uniform(0,100)
        round_quantity = round(random_num,1)
        number_list.append(round_quantity)

def append_random_words(words_list, quantity=1):
    for _ in range(quantity):
        random_word = random.words_list
        words_list.append(random_word)
main()