rows, cols = 2, 3
r = 0
while r < rows:
    c = 0
    while c < cols:
        print(f"({r},{c})", end=' ')
        c += 1
    print()
    r += 1
