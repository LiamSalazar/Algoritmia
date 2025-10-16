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
        i = array.index(pivot)
        maximo(array[:i],count+1)
        maximo(array[i+1:], count+1)
    
    maximo(array, count)
    i = 0
    for v in dict.values():
        if i == len(dict):
            print(v)
        else:
            print(v, end=" ")

