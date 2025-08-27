"""
    Idea: Use helper array.
    Time Complexity: O(n)
    Space Complexity: O(n)
"""
def solution(A, K):
    n = len(A)
  
    # Check if the rotated array will be the same as the original
    if n <= 1 or K % n == 0:
        return A
    
    # Avoid unnecessary full rotations
    while K > n:
        K -= n

    # Initialize a new array to store the rotated result
    cycled_array = [0] * n

    # Rotate the array by placing each element at its new position
    for i in range(n):
        cycled_array[(i + K) % n] = A[i]
    
    return cycled_array