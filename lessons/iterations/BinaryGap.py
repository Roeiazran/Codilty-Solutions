"""
    Idea: Strip the number from any rightmost zeros, and examine the binary number last digit, at any occurrence of 1 update the maximum gap seen so far.
    Complexity: O(n) where n is the number of bits in the binary representation on N.
"""
def solution(N):

    temp_max_gap = max_gap = 0

    if N == 0:
        return 0
    
    # lose trailing zeros
    while (N % 2 == 0): 
        N //= 2

    # strip the rightmost 1 bit
    N //= 2

    while (N):

        if N % 2 == 0:
            temp_max_gap += 1

        if N % 2 == 1:
            max_gap = max(max_gap, temp_max_gap) # set the max gap seen so far
            temp_max_gap = 0 # reset the current gap to 0

        N //= 2

    return max_gap