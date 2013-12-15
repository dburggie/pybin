def iton(i):
    i = int(i)
    output = ''
    
    # store bytes in a stack
    stack = []
    for things in range(4):
        stack.append( i % 256 )
        i /= 256

    # pop bytes off of stack into output string
    for things in stack[:]:
        output += itoc(stack.pop())
    return output
