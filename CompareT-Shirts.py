t = int(input())
for _ in range(t):
    a, b = input().strip().split()

    if a == b:
        print("=")
        continue

    letra_a, letra_b = a[-1], b[-1]        
    if letra_a != letra_b:
        dict = {'S': 0, 'M': 1, 'L': 2}
        print("<" if dict[letra_a] < dict[letra_b] else ">")
        continue

    nXa = a.count('X')
    nXb = b.count('X')

    if letra_a == 'S':
        print("<" if nXa > nXb else ">")
    else:  
        print(">" if nXa > nXb else "<")
