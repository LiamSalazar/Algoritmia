t = int(input())
for _ in range(t):
    s = input()
    if len(s) % 2 != 0 or s[0] == ')' or s[-1] == '(':
        print("NO")
        continue

    min_open = 0
    max_open = 0

    for c in s:
        if c == '(':
            min_open += 1
            max_open += 1
        elif c == ')':
            min_open -= 1
            max_open -= 1
        else:  # '?'
            min_open -= 1
            max_open += 1

        if max_open < 0:
            print("NO")
            break
        min_open = max(min_open, 0)
    else:
        print("YES" if min_open == 0 else "NO")
