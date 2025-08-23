
# B =< A <= 2B + 2
def solution(A, B):

    res = ""
    if A > B:
        while A > B and A - 2 > 0 and B > 0:
            A -= 2
            B -= 1
            res += "aab"

        # or A = B or A = B + 1 or A = B + 2
        if A == B:
            return res + "ab" * A

        return res + "ab" * B + "a" * (A - B) # A = B + 1 or A = B + 2
        
    elif B > A:
        while B > A and B - 2 > 0 and A > 0:
            B -= 2
            A -= 1
            res += "bba"
        
        if A == B:
            return res + "ab" * A
        
        return res + "ba" * A + "b" * (B - A)
    
    else:
        return "ab" * A


print(solution(8,4))