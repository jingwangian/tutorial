def quick_find_fail(P):
    m = len(P)
    fail = [0]*m
    j = 1
    k = 0
    while j < m:
        if P[j] == P[k]:
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return fail

def quick_find(T,P,pos):
    n, m = len(T),len(P)
    if m == 0:
        return 0
    fail = quick_find_fail(P)
    j = pos
    k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m-1:
                return j- m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return -1

def search2(text, sub_text):
    text = text.lower()
    sub_text = sub_text.lower()

    pos = 0
    while True:
        pos = quick_find(text, sub_text,pos)
        if pos != -1:
            pos += 1
            yield pos
        else:
            break