"""
    Idea: The maximum profit achievable is the largest profit from buying at price A[i] and selling at a higher price later in the array.
    Traverse the array from left to right, keeping track of the maximum value seen so far. For each index, calculate max_value - A[i]. The largest of these values is the maximum profit.
    Complexity: O(n)
"""
def solution(A):
    n = len(A)
    m = 0 # stores the maximum value seen so far
    mp = 0 # stores the maximum profit seen so far

    for i in range(n - 1, -1, -1):
        m = max(m, A[i])
        mp = max(mp, m - A[i])

    return mp