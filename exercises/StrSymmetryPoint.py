
def solution(S):

    n = len(S)

    if n == 1:
        return 0
    
    if n % 2 == 0:
        return -1
    
    if S[::-1] == S:
        return n // 2
    
    return -1



print(solution("a"))