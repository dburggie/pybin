def ntoi(s):
    l = 0
    stack = []
    for c in s:
        stack.append(c)
    for c in stack[:]:
        l *= 256
        l += ctoi(stack.pop())
    return l
