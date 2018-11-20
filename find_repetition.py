from os import listdir

def find_repetition(path):


    k=0
    m=0
    lista=[]
    duplicate = []
    testListDict = {}

    for val in listdir(path):
        file = open(path+val,"rb")
        c = file.read()
        lista.insert(k,c)
        if c  in testListDict:
            e= lista.index(c)
            testListDict[c] += 1
            stri = listdir(path).__getitem__(k)+" e' un duplicato "+listdir(path).__getitem__(e)
            duplicate.insert(m, stri)
            m+=1
        else:
            testListDict[c]=1
        k+=1
        file.close()



    return duplicate


path = "/Users/VALE/Desktop/testi/"

print(find_repetition(path))
