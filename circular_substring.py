"""
Diciamo che un pattern P di lunghezza m è una sottostringa circolare di un testo T di
lunghezza n > m se P e una sottostringa (normal) di T oppure se P è uguale ad una
concatenazione di un suffisso di T ed un prefisso di T, cioè se esiste un indice 0 <= k < m,
tale che P = T [n − m + n : n] + T [0 : k].
Implementare la funzione circular_substring(P, T) che restituisce True se P è una
sottostringa circolare di T e False altrimenti. La funzione deve avere complessità O(m +
n).
"""
#O(m+n)
from TdP_collections.text.find_kmp import *

def circular_substring(P,T):
    n, m = len(T), len(P)
    if m == 0: return False
    if n < m: return False
    fail = compute_kmp_fail(P)
    status = 0
    j = 0
    k = 0
    while j < n:
        #print(T[j],P[k],j,k,n)
        if T[j] == P[k]:
            if k == m - 1 :
                return True
            j += 1
            k += 1
            if j == n:
                j = 0
                status = 1
                n=m-k
        elif k > 0:
            if status == 0:
                k = fail[k-1]
            else:
                break
        else:
            j += 1
    return False

if __name__ == '__main__':
    T="ciaomondo"
    P="ond"
    print(circular_substring(P,T))#True

    P="nm"
    print(circular_substring(P,T))#False

    P="dociao"
    print(circular_substring(P,T))#True

    P="docao"
    print(circular_substring(P,T))#False



