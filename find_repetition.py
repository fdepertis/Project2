
from os import listdir
path = "/Users/VALE/Desktop/testi/"
lista=[]

k=0
list=listdir(path)
size =list.__len__()-1

for val in listdir(path):
    file = open(path+val,"r")
    content = file.read()
    lista.insert(k,content)
    k+=1
    file.close()


duplicate =[]


d=0
for i,val in enumerate(lista):
    for j,val2 in enumerate(lista):
        if(val == val2):
            if (list.__getitem__(i) in duplicate) == 0 and i!=j :
               testo = list.__getitem__(j)+" e' uguale a "+list.__getitem__(i)
               duplicate.insert(d,testo)
               d+=1



print(duplicate)
