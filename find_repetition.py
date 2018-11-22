from os import listdir



def find_repetition(path):

    dup = []
    duplicate = {}
    fileset = set()

    for val in listdir(path):
        file = open(path+val,"r")
        c = hash(file.read())
        file.close()
        if c in fileset:
            duplicate[c].append(val)
        else:
            fileset.add(c)
            duplicate[c]=[val]
        

    for val in duplicate.values():
        if(len(val)>1):
            dup.append(val)


    return list(dup)


path = "/Users/VALE/Desktop/testi/"
print(find_repetition(path))
