import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiDict = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        txtIn_ripulito = replaceChars(txtIn)
        parole = txtIn_ripulito.lower().split(" ")
        paroleErrate = []
        for p in self.multiDict.searchWord(parole, language):
            if not p.corretta:
                paroleErrate.append(p)
        return paroleErrate


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\'*_{}[]()>#+-.!?$%^,=_"
    for c in chars:
        text = text.replace(c, "")
    return text

def _test_spellChecker():
    print(__name__)
    txt = replaceChars("Ciao, come ti chiami?")
    print(txt)

if __name__ == "__main__":
    _test_spellChecker()