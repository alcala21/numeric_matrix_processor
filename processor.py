n1, m1 = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(n1)]
constant = int(input())
B = [[constant*int(x) for x in row] for row in A]
for row in B:
    print(*row)
