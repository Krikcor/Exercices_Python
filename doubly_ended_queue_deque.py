from collections import deque

def supprime_extremites_optimise(liste, n):
    d = deque(liste)
    while n > 0:
        d.popleft()
        d.pop()
        n -= 1
    return list(d)