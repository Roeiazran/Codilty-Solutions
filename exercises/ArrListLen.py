
def solution(A):

    length = 0

    k = 0
    while k != -1:
        k = A[k]
        length += 1

    return length


print(solution([1,4,-1, 3, 2]))