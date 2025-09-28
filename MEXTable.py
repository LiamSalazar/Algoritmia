testcases = int(input())
for testcase in range(testcases):
    n, m = map(int, input().split())
    print(max(n, m) + 1)