import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dict = d.Dictionary()

    def printDic(self, language):
        self.dict.loadDictionary(f"resources/{language}.txt")
        self.dict.printAll()

    def searchWord(self, words, language):
        lista_rw = []
        self.dict.loadDictionary(f"resources/{language}.txt")
        for w in words:
            rich_word = rw.RichWord(w)
            #for p in self.dict.dict:
                #if w == p:
                    #rich_word.is_corretta(True)
                    #break
            #lista_rw.append(rich_word)
        #return lista_rw

            if self.dict.dict.__contains__(w):
                rich_word.is_corretta(True)
            lista_rw.append(rich_word)
        return lista_rw


def _test_multiDictionary():
    print(__name__)
    md = MultiDictionary()
    print(md.searchWord(["aad", "ba"], "italian"))

if __name__ == "__main__":
    _test_multiDictionary()