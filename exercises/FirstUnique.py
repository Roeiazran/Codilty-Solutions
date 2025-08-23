
def solution(A):

    d = {}

    for item in A:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1

    for item in A:
        if d[item] == 1:
            return item
    return -1


print(solution([1,1,4,2,3]))