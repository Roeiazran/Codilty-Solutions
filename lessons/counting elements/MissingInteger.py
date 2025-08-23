
def solution(A):
   
    n = len(A)
    A.sort()
    search_index = 0

    # find the first index of a positive number
    for item in A:
        if item <= 0:
            search_index = search_index + 1
        else:
            break
    
    # if all array in negative or the first positive is not 1
    if search_index == n or A[search_index] != 1:
        return 1
    
    for i in range(search_index, n - 1):
        # check for (x, x + n) s.t n > 1

        if A[i + 1] - A[i] > 1:
            return A[i] + 1
    
    # missing the n + 1 item
    return A[n - 1] + 1