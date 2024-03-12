import random
import string
import sys
from random import shuffle
import re

from typing import List


class Anagram:

    def __init__(self, word: str, token: int = 0):
        self.word = word if Anagram._check_word(word) else Anagram._random_word()
        self.token = token

    @staticmethod
    def _random_word() -> str:
        """
        Method to generate a list of letter if no world is given.

        :return:  a block of letter
        """
        return "".join(random.sample(list(string.ascii_lowercase), k=random.randint(1, 26)))

    @staticmethod
    def _check_word(word: str) -> bool:
        """
        Static method to check that the word in parameter is word and not a pure digit or
        a mixture of letters and digit.

        :param word: the word given in parameter
        :return: True if the word is a pure string with letters
        """
        check = bool(re.search(r'\d', word))
        return True if not check else False

    def _shuffle_word(self) -> str:
        """
        Method to shuffle the letter of a word and make a new word.
        :return: un new word
        """
        a = list(self.word)
        shuffle(a)
        return "".join(a)

    # choice of shuffle
    def start_research(self) -> List[str]:
        """
        Method to generate a list of new words.
        :return: a list of new words
        """
        anagrams = []
        shuffle_number = None
        counter = 0
        while shuffle_number is None or shuffle_number.isdigit() is False:
            shuffle_number = input("[?] Give a number of run you want : >> ")
        research_int = int(shuffle_number)
        while not counter == research_int:
            result = self._shuffle_word()
            if result != self.word:
                anagrams.append(result)
            counter += 1
        if self.token == 0:
            self.reload_search()
        else:
            return anagrams

    # again a shuffle or shutdown the program?
    def reload_search(self) -> None:
        """Method to restart a shuffle with the same word"""
        query = input(">> Start again the search of an anagram ?! >> [o/n]")
        if query.lower() == "o":
            self.start_research()
        else:
            sys.exit(0)


# ---------------------------program-----------------------------
print("Hello, this is a small program to find an anagram randomly.")
print()
mot = ''
while mot == '':
    mot = input("[?] Give a word, please. \n(if none, a default list of letters will be generated.\n >> ")

mot_str = Anagram(mot, 0)
mot_str.start_research()
