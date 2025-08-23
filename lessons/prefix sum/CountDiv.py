
def solution(A, B, K):
    
    # get upper and lower bounds in range that devide by K
    u = B - (B % K)
    l = A + (K - A % K)

    # total = (diff / k) + 1 to include one of the boudries
    t = (u - l) // K + 1 

    # because l = A + K in that case
    if A % K == 0: 
        return t + 1

    return t