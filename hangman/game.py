import random


class Hangman:
    def __init__(self, number_of_mistakes):
        self.mistakes_remaining = number_of_mistakes
        self.word = None
        self.visible_word = None
        self.entered_letters = set()

    def generate_word(self):
        with open(r"data/WordsStockRus.txt", "r", encoding="utf-8") as file:
            all_words = file.readlines()
            chosen_word = random.choice(all_words)
            self.word = chosen_word[:-1]
            self.visible_word = list("_" * len(self.word))

    def get_visible(self):
        return self.visible_word

    def get_mistakes_remaining(self):
        return self.mistakes_remaining

    def get_entered_letters(self):
        return sorted(self.entered_letters)

    def turn(self, user_try):
        self.entered_letters.add(user_try)
        if user_try in self.word:
            for i, letter in enumerate(self.word):
                if user_try == letter:
                    self.visible_word[i] = letter
        else:
            self.mistakes_remaining -= 1
        return self.visible_word

def got_invalid_input():
    return "Некорректный ввод!"
