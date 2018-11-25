from TdP_collections.hash_table.probe_hash_map import ProbeHashMap
from os import listdir

def find_repetition(dir):
    hashmap = ProbeHashMap()
    duplicate = list()

    for val in listdir(dir):
        file = open(dir + val, "r")     # apre il file
        c = hash(file.read())           # hash associato al testo del file letto
        file.close()                    # chiudo il flusso del file
        if c not in hashmap:            # vedo se l'hash è gia presente nel set, usiamo i set perché la ricerca ha complessità O(1)
            hashmap[c] = [val]          # append con chiave valore su duplicare che è un dizionario
        else:
            hashmap[c].append(val)      # se non è gia presente nell'hash aggiungo a duplicate la coppia chiave valore nuova

    for l in hashmap.values():          # serve per inserire in dup (ovvero il vettore che ritorneremo) solo quelli con occorrenze maggiori di 1
        if (len(l) > 1):
            duplicate.append(l)
    return duplicate

if __name__ == '__main__':
    print("Lista dei file duplicati nella directory 'dir'")
    for i in find_repetition("./dir/"):
        print(i)
