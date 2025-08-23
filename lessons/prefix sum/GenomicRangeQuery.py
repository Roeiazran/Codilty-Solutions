
def solution(S, P, Q):

    N = len(S)
    n = len(P)
    res = [0] * n
    ones = [-1] * N
    twos = [-1] * N
    threes = [-1] * N
    min1 = -1
    min2 = -1 
    min3 = -1
    
    for i in range(N):
        if S[i] == 'A':
            min1 = i
        elif S[i] == 'C':
            min2 = i
        elif S[i] == 'G':
            min3 = i

        ones[i] = min1
        twos[i] = min2
        threes[i] = min3

 
    for i in range(n):
        if ones[Q[i]] >= P[i]:
            res[i] = 1
        elif twos[Q[i]] >= P[i]:
            res[i] = 2
        elif threes[Q[i]] >= P[i]:
            res[i] = 3
        else:
            res[i] = 4
    
    return res