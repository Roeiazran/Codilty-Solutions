def soltion(A):

    n = len(A)
    size = 0

    for k in range(n):
        if size == 0:
            size = 1
            value = A[k]
        elif value != A[k]:
            size -= 1
        else: 
            size += 1
    
    if size == 0:
        return -1
    
    counter = 0
    for k in range(n):
        if A[k] == value:
            saved = k
            counter += 1
        
    if counter > n // 2:
        return saved

    return -1
    
