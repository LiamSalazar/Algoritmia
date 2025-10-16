testcases = int(input())
for _ in range(testcases):
    s = (input())
    valid = 0
    open = 0
    close = 0
    s_noSign = s.replace('?', '')
    signs = len(s) - len(s_noSign)
    if len(s) % 2 != 0 or s[0] == ')' or s[-1] == '(':
        print("NO")
        continue
    for e in s_noSign:
        if e == '(':
            valid += 1
            open += 1
        elif e == ')':
            valid -= 1
            close += 1
    if open == close and valid == 0:
        print("YES")
        continue
    elif abs(open - close) > signs:
        print("NO")
        continue
    else:
        print("YES")
        # (?(?)) = YES - > ((())) 
        #((?))) = YES -> ((())))
        # ())(()

