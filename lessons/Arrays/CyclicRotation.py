
def solution(A, K):
    n = len(A)

    if n <= 1 or K % n == 0:
        return A
    
    while K > n:
        K -= n

    cycled_array = [0] * n

    for i in range(n):
        
        cycled_array[(i + K) % n] = A[i]
    
    return cycled_array

print(solution([-1, -2, -3, -4, -5, -6], 10))

