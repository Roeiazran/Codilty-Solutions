
# N = 24, 12, 6, 3 
# N = 26, 13
# N = 8, 4, 2, 0

def solution(N):

    if N % 2 == 1:
        return 0
    
    parity = 0
    while N % 2 == 0:
        N /= 2
        parity += 1
        if not N:
            break
    
    return parity


print(solution(26))