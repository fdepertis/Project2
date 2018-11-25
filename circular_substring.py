from TdP_collections.text.find_kmp import compute_kmp_fail

def circular_substring(P, T):
    n, m = len(T), len(P)
    if m == 0 or n < m:
        return False
    fail = compute_kmp_fail(P)
    status = False
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
                status = True
                n=m-k
        elif k > 0:
            if not status:
                k = fail[k-1]
            else:
                break
        else:
            j += 1
    return False

if __name__ == '__main__':
    T="ciaopierpaolo"
    P="pier"
    print(circular_substring(P,T))#True

    P="pietro"
    print(circular_substring(P,T))#False

    P="paolociao"
    print(circular_substring(P,T))#True

    P="paolocisei"
    print(circular_substring(P,T))#False



