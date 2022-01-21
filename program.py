#row operation
for row in range (0, 5):
    n = 1
    # column operation
    for column in range (0, row+1):
        print(n, end=" ")
        n = n+1
    # ending line
    print('\r')
