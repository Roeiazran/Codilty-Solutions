
def prefix_sum(A, n) :
  
    prefix = [0] * n
    prefix[0] = A[0]

    for i in range(1, n) :
        prefix[i] = prefix[i - 1] + A[i]

    return prefix

def solution(A):
    
    n = len(A)
    p = prefix_sum(A, n)
    ts = 0
   
    for i in range(n):
        if A[i] == 0:
            ts = ts + p[n - 1] - p[i]

    if ts > 1000000000:
        return -1
        
    return ts