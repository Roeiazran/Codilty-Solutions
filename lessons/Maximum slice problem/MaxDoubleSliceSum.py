
def solution(A):

    N = len(A)
    l = [0] * N
    r = [0] * N
    l[0] = 0
    r[N - 1] = 0

    for i in range(1, N):
        l[i] = max(0, l[i - 1] + A[i])

    for i in range(N - 2, -1, -1):
        r[i] = max(0, r[i + 1] + A[i])

    m = 0
    for i in range(1, N - 1):
        m = max(m, l[i - 1] + r[i + 1])

    return m