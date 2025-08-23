

# 1041 -> 10000010001
def solution(N):

    temp_max_gap = max_gap = 0

    if N == 0:
        return 0
    
    # loosing trailing zeros
    while (N % 2 == 0): 
        N //= 2
        
    # strip the first 1
    N //= 2

    while (N):

        if N % 2 == 0:
            temp_max_gap += 1

        if N % 2 == 1:
            max_gap = max(max_gap, temp_max_gap)
            temp_max_gap = 0
        N //= 2

    return max_gap


print(solution(7))