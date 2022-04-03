import os
import random

from Game import Game


def clear_console():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


class Hangman(Game):
    words = [
        'member',
        'precision',
        'pocket',
        'disturbance',
        'effective',
        'weapon',
        'chemistry',
        'publication',
        'understand',
        'extraterrestrial'
    ]
    difficulty = {
        'BEGINNER': 8,
        'INTERMEDIATE': 5,
        'ADVANCED': 3
    }

    def __init__(self):
        self.players = 0
        self.mistakes = 0
        self.maxMistakes = 0
        self.guessedLetters = []
        self.lettersToGuess = []
        self.word = ""

    def select_mode(self):
        while self.players == 0:
            clear_console()
            print("How may players(1 or 2)?")
            p = input()
            if p == '1' or p == '2':
                self.players = int(p)

    def select_difficulty(self):
        while self.maxMistakes == 0:
            clear_console()
            print("Select difficulty level!")
            print("BEGINNER/INTERMEDIATE/ADVANCED")
            p = input()
            if p.upper() in ['BEGINNER', 'INTERMEDIATE', 'ADVANCED']:
                self.maxMistakes = self.difficulty[p.upper()]

    def start_game(self):
        self._play()

    def _play(self):
        self.select_mode()
        self.select_difficulty()
        super()._play(self.players)

        if self.players == 1:
            self.word = self.words[random.randint(0, len(self.words) - 1)]
            self.play_single()
        elif self.players == 2:
            self.play_multi()

    def play_single(self):
        self.lettersToGuess = set(self.word)
        print(self.word)
        while self.mistakes < self.maxMistakes and len(self.lettersToGuess) > 0:
            clear_console()
            self.print_covered_word()
            letter = input('\nType Letter: ')
            if self.lettersToGuess.__contains__(letter):
                self.guessedLetters.append(letter)
                self.lettersToGuess.remove(letter)
            else:
                self.mistakes += 1
            print('Possible mistakes: ', self.maxMistakes - self.mistakes)
        if len(self.lettersToGuess) == 0:
            self.print_covered_word()
            print('\nYou won!')
        else:
            print('You lost!')

    def play_multi(self):
        self.word = input("Type a word: ")
        clear_console()
        self.play_single()

    def print_covered_word(self):
        for x in self.word:
            if self.guessedLetters.__contains__(x):
                print(x, end='')
            else:
                print("_", end='')


game = Hangman()
game.start_game()
