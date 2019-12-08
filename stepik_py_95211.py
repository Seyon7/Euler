n = int(input())
squeares = [i for i in range(1, n ** 2 + 1)]
spiral = [[0] * n for i in range(n)]


for i in spiral:
    for j in i:
        print(j, end=" ")
    print()
