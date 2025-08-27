"""
    Idea: Sort the array and find index i s.t A[i + 1] - A[i] > 1.
    Complexity: O(n*log(n))
"""
def solution(A):
    n = len(A)
    A.sort()
    search_index = 0

    if n == 0: return 1

    # find the first index of a positive number in A
    while search_index < n and A[search_index] < 0: search_index += 1
    
    # if all array in negative or the first positive is not 1
    if search_index == n or A[search_index] != 1:
        return 1
    
    for i in range(search_index, n - 1):

        # check for (x, x + n) s.t n > 1
        if A[i + 1] - A[i] > 1:
            return A[i] + 1
    
    # missing the n + 1 item
    return A[n - 1] + 1