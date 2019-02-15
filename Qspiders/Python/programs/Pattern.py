n = 5
asciiVal = ord('I')
l = 6
for i in range(1, n+1):
    for j in range(1, n+1):
        if i <= j:
            if i % 2 == 1:
                print(chr(asciiVal), end=' ')
                asciiVal -= 1
            else:
                print(l, end=' ')
                l -= 1
        else:
            print(' ', end=' ')
    print()
