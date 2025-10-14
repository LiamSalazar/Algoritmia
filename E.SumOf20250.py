testcases = int(input())
for _ in range(testcases):
    n = int(input())
    if n%2050 != 0 or n < 2050:
        print(-1)
    else:
        n //= 2050
        r = 0
        while n > 0:
            r += n % 10
            n //= 10
        print(r)
