
def solution(A):
    
    a = 0
    b = A[0]

    for i in A:
        a = max(i, a + i)
        b = max(a, b)

    return b