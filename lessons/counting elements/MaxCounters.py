
def solution(N, A):

    max_val = curr_max_value = 0
    counters = [0] * N
    
    for i in range(len(A)):
        index = A[i] - 1

        if A[i] == N + 1:
            max_val = curr_max_value
        
        else: 
            counters[index] = max(counters[index], max_val) + 1
            curr_max_value = max(curr_max_value, counters[index])
    
    for i in range(N):
        if counters[i] < max_val:
            counters[i] = max_val

    return counters


print(solution(5, [1,2,3,4,5, 6, 2, 2]))