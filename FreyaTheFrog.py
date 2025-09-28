testcases = int(input())
for testcase in range(testcases):
    x, y, k = map(int, input().split())
    
    minimo_x = x // k
    if x % k != 0:  
        minimo_x += 1
    minimo_y = y // k
    if y % k != 0:
        minimo_y += 1
    
    par = 2 * max(minimo_x, minimo_y)
    impar = 2 * max(minimo_y, minimo_x - 1) + 1
    print(min(par, impar))
