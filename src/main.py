
from random import shuffle
import re


class Word:

    def __init__(self, word, token=0):
        self.word = word
        self.token = token

    # function shuffle for a word
    def anagramme(self):
        a = list(self.word)
        shuffle(a)
        return "".join(a)

    # choice of shuffle
    def anagramme_multiple(self, token):
        nombre_de_recherche = ''
        y = 1
        while nombre_de_recherche == '' or nombre_de_recherche.isdigit() == False:
            nombre_de_recherche = input("Choisissez le nombre d'anagramme à générer:")
        nombre_de_recherche_int = int(nombre_de_recherche)
        print(f"Voici les résultats pour {nombre_de_recherche} anagrammes du mot ({self.word}):")
        print()
        while y <= nombre_de_recherche_int:
            print("".join(self.anagramme()))
            y = y+1
        if token == 0:
            self.relance_anagramme()
        else:
            exit()

    # again a shuffle or shutdown the program?
    def relance_anagramme(self):
        question = input("Relancez le générateur avec le même mot ? o/n")
        if question.lower() == "o":
            self.anagramme_multiple(1)
        elif question.lower() == "n":
            print("Ok. Programme Terminé")
        else:
            print("Vous n'avez pas donné de réponse valide. Programme Terminé")
            self.relance_anagramme()


    # check if it's a word or number // miss to block the mixture of word+number
    def verification_anagramme(self):
        m = self.word
        bool(re.search(r'\d', m))
        if True:
            print(f"Erreur, vous n'avez pas inscrit un mot, recommencez s'il vous plait.")
            self.word = input("Quel est votre mot ? :")
            self.verification_anagramme()
        else:
            return


# ---------------------------program-----------------------------
'''if __name__ == '__main__':
    AnagramApp().run()'''
print("Bonjour, ceci est un petit programme pour trouver un anagramme aléatoirement.")
print()
mot = ''
while mot == '':
    mot = input("Veuillez donner un mot :")

mot_str = Word(mot)
mot_str.verification_anagramme()
mot_str.anagramme_multiple(0)
# mot_str.relance_anagramme()
