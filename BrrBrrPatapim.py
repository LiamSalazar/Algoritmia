testcases = int(input())
for test in range(testcases):
    n = int(input())
    G = [list(map(int, input().split())) for row in range(n)]
    permutacion = [0 for elem in range(2 * n)]
    elementos_irrepetibles = set(range(1, (n+n) + 1))

    for i in range(n):
        for j in range(n):
            elementos_irrepetibles.discard(G[i][j])          
            indice = i + j + 1              
            permutacion[indice] = G[i][j]

    permutacion[0] = elementos_irrepetibles.pop()

    for i in range(2 * n):
        if i + 1 == (2 * n):
            print(permutacion[i])
        else:
            print(permutacion[i], end=" ")
