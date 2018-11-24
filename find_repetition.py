from os import listdir

def find_repetition(path):
    dup = []
    duplicate = {}
    fileset = set()

    for val in listdir(path):
        file = open(path + val, "r")  # apre il file
        c = hash(file.read())  # hash associato al testo del file letto

        file.close()  # chiudo il flusso del file
        if c in fileset:  # vedo  se l'hash è gia presente nel set ...usiamo i set perchè la ricerca ha complessità O(1)
            duplicate[c].append(val)  # append con chiave valore su duplicare che è un dizionario
        else:
            fileset.add(c)  # se non è gia presente nell'hash aggiungo a duplicate la coppia chiave valore nuova
            duplicate[c] = [val]

    for val in duplicate.values(): # serve per inserire in dup ( ovvero il vettore che ritorneremo) solo quelli con occorrenze maggiori di 1
        if (len(val) > 1):
            dup.append(val)

    return list(dup)

if __name__ == '__main__':
    path = "../Progetto2/testi/"
    print(find_repetition(path))
