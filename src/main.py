import random
import string
import re
from random import shuffle
from typing import List


class Anagram:

    def __init__(self, word: str):
        self.word = word if (Anagram._check_word(word) and word != "") else Anagram._random_word()
        self.anagrams = None

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
    def start_research(self) -> None:
        """
        Method to generate a list of new words.
        :return: a list of new words
        """
        anagrams = self.anagrams if self.anagrams else []
        shuffle_number = None
        counter = 0
        while shuffle_number is None or shuffle_number.isdigit() is False or shuffle_number == '0':
            shuffle_number = input("[?] Give a number of research you want : >> ")
        research_int = int(shuffle_number)
        while not counter == research_int:
            shuffle_result = self._shuffle_word()
            if shuffle_result != self.word:
                anagrams.append(shuffle_result)
            counter += 1
        self.anagrams = list(set(anagrams))
        self.reload_search(self.anagrams)

    def reload_search(self, new_words: List[str]) -> List[str]:
        """Method to restart a shuffle with the same word"""
        query = input(">> Start again the search of an anagram ?! >> [o/n]")
        if query.lower() == "o":
            self.start_research()
        else:
            return new_words


# ---------------------------program-----------------------------
print("Hello, this is a small program to find an anagram randomly.")
print()
mot = input("[?] Give a word, please. \n(if none, a default list of letters will be generated.\n >> ")

start = Anagram(mot)
result = start.start_research()
print(result)
