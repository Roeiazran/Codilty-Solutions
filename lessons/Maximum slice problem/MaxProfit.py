
def solution(A):
    
    n = len(A)
    m = 0
    mp = 0

    for i in range(n - 1, -1, -1):
        m = max(m, A[i])
        mp = max(mp, m - A[i])

    return mp

