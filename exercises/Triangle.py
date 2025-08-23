
def solution(A):
    A.sort()
    n = len(A)
    si = 0
    for i in range(n):
        if A[i] > 0:
            break
        si = si + 1

    for i in range(si, n - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1

    return 0

        