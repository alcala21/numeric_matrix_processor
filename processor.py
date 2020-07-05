n1, m1 = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(n1)]
n2, m2 = [int(x) for x in input().split()]
B = [[int(x) for x in input().split()] for _ in range(n2)]
if n1 == n2 and m1 == m2:
    C = [[a + b for a, b in zip(x, y)] for x, y in zip(A, B)]
    for row in C:
        print(*row)
else:
    print("ERROR")
