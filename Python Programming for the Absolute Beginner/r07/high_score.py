import shelve

def high_scores(score):
    name = input("\nWprowadz swoja nazwe --> ")

    sFile = shelve.open("high_scores.dat")
    sFile[name] = [name, score]

    print("\n+ WYNIK +\n")
    for entries in sFile:
        print(sFile[entries][0],sFile[entries][1])

    sFile.close()
    return "Test"