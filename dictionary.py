class Dictionary:
    def __init__(self):
        self._parole = []

    def loadDictionary(self,path):
        with open(path, 'r') as file:
            for line in file:
                parola = line.splitlines()[0]
                self.dict.append(parola)

    def printAll(self):
        for p in self.dict:
            print(p)


    @property
    def dict(self):
        return self._parole


def _test_dictionary():
    print(__name__)
    d = Dictionary()
    d.dict.append('parole')
    print(d.dict)
    d.loadDictionary("resources/Italian.txt")
    print(d.dict)
    d.printAll()

    lista = ['ciao', 'bello', 'pompino']
    if lista.__contains__("ciau"):
        print("SI!")
    else:
        print("NO!")

if __name__ == "__main__":
    _test_dictionary()