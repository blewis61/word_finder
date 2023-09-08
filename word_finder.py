from itertools import permutations

with open('collins_scrabble_words.txt', 'r') as file:
    dictionary = set(word.strip() for word in file)

letters = input("Please input 7 letters: ")

def word_finder(letters):
    """Accepts a string of letters and outputs all words between 3 and 7 letters long"""
    possible_words = set()
    three_letter_words = []
    four_letter_words = []
    five_letter_words = []
    six_letter_words = []
    seven_letter_words = []

    for length in range(3, 8):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            possible_words.add(word.upper())

    for word in possible_words:
        if word in dictionary:
            if len(word) == 3:
                three_letter_words.append(word)
            elif len(word) == 4:
                four_letter_words.append(word)
            elif len(word) == 5:
                five_letter_words.append(word)
            elif len(word) == 6:
                six_letter_words.append(word)
            else:
                seven_letter_words.append(word)
    
    print(f"3 Letter Words: {three_letter_words}")
    print(f"4 Letter Words: {four_letter_words}")
    print(f"5 Letter Words: {five_letter_words}")
    print(f"6 Letter Words: {six_letter_words}")
    print(f"7 Letter Words: {seven_letter_words}")

word_finder(letters)