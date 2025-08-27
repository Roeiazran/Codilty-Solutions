"""
    Idea: The maximum slice sum is the largest sum of any contiguous 
    subarray of A. For each index, compute the maximum sum of a subarray 
    ending at that index, and return the largest of these sums. (kadane's algorithm)
    Complexity: O(n)
"""
def solution(A):
    
    a = 0
    b = A[0]

    for i in A:
        a = max(i, a + i)
        b = max(a, b)

    return b