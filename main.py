import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        paroleErrate = sc.handleSentence(txtIn, "italian")
        if len(paroleErrate) == 0:
            print("La frase è corretta")
        else:
            print(f"La frase è errata, gli errori sono {len(paroleErrate)}:")
            for p in paroleErrate:
                print(p)
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        paroleErrate = sc.handleSentence(txtIn,"english")
        if len(paroleErrate) == 0:
            print("La frase è corretta")
        else:
            print(f"La frase è errata, gli errori sono {len(paroleErrate)}:")
            for p in paroleErrate:
                print(p)
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        paroleErrate = sc.handleSentence(txtIn,"spanish")
        if len(paroleErrate) == 0:
            print("La frase è corretta")
        else:
            print(f"La frase è errata, gli errori sono {len(paroleErrate)}:")
            for p in paroleErrate:
                print(p)
        continue

    if int(txtIn) == 4:
        break


