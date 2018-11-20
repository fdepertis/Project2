from os import listdir

def find_repetition(path):
    dict=[]
    k=0
    list=listdir(path)

    for val in listdir(path):
        file = open(path+val,"r")
        content = file.read()
        dict.insert(k,content)
        k+=1
        file.close()

    duplicate =[]
    testListDict = {}
    l=0
    m=0

    for item in dict:
        if item  in testListDict:
            c= dict.index(item)
            testListDict[item] += 1
            stri = list.__getitem__(l)+" è un duplicato di "+list.__getitem__(c)
            duplicate.insert(m, stri)
            m += 1
        else :
            testListDict[item] = 1

        l+=1

    return duplicate


path = "/Users/VALE/Desktop/testi/"

print(find_repetition(path))
