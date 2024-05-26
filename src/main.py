import re
import requests
from random import shuffle
from typing import List, Union


class Anagram:

    def __init__(self, word: str):
        self.word = word if (Anagram._check_word(word) and word != "") else Anagram._random_word()
        self.anagrams = None

    @staticmethod
    def _random_word() -> str:
        """
        Method to generate a word from the call of RANDOM WORDS API.

        :return:  a word from the English dictionary
        """
        api_url = "https://random-word-api.herokuapp.com/word"
        return requests.get(url=api_url).text.strip('[]"')

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
        anagrams = self.anagrams if self.anagrams else []
        shuffle_number = None
        count = 0
        while shuffle_number is None or shuffle_number.isdigit() is False or shuffle_number == '0':
            shuffle_number = input("[?] Give a number of research you want :\n >> ")
        research_int = int(shuffle_number)
        while not count == research_int:
            shuffle_result = self._shuffle_word()
            if shuffle_result != self.word:
                anagrams.append(shuffle_result)
            count += 1
        self.anagrams = list(set(anagrams))
        return self.anagrams

    def reload_search(self) -> Union[List[str], None]:
        """Method to restart a shuffle with the same word"""
        query = input(">> Do you want to make a new research with the same word ?!\n [y/n] >>")
        if query.lower() == "y":
            self.start_research()
        return self.anagrams


# ---------------------------program-----------------------------
print("Hello, this is a small program to generate an anagram randomly.")
print()
mot = input("[?] Give a word, please. \n(if none, a default word will be generated.)\n >> ")

start = Anagram(mot)
result = start.start_research()
counter = 1
for res in result:
    print(f"Anagram n° {counter} : '{res}'")
    counter += 1
again = start.reload_search()
for a in again:
    print(f"Anagram n° {counter} : '{a}'")
    counter += 1
