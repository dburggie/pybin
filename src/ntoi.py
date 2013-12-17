from ctoi import ctoi

def ntoi(n):
    i = 0
    for c in n:
        i *= 256
        i += ctoi(c)
    return i
