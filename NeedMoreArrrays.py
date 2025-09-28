testcases = int(input())
for _ in range(testcases):
    n = int(input())
    a = list(map(int, input().split()))
    distintos = []
    for num in a:
        if not distintos or distintos[-1] != num:
            distintos.append(num)
    r = 0
    longitud = 0
    anterior = None
    for num in distintos:
        if anterior is None or num != anterior + 1:
            if longitud > 0:
                r += (longitud + 1) // 2
            longitud = 1
        else:
            longitud += 1
        anterior = num
    if longitud > 0:
        r += (longitud + 1) // 2
    print(r)