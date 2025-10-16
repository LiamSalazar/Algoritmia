testcases = int(input())
for _ in range(testcases):
    n = int(input())
    array = list(map(int, input().split()))
    dict = {}
    for e in array:
        dict[e] = -1
    
    count = 0
    
    def maximo(array, count):
        if not array:
            return
        pivot = max(array)
        dict[pivot] = count
        count+=1
        maximo(array[:pivot],count)
        maximo(array[pivot:], count)
    
    maximo(array, count)
    print(dict)

