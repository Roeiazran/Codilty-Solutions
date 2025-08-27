"""
    Idea: Keep the maximum value that all counters should have as minimum value, 
    and set it as the lower bound to any counter value before incrementing it.
    Complexity: O(n) - Keeping the maximum allows to record the minimum value of each counter and instead of 
    incrementing all counter when A[i] == N + 1 we update any counter with that lower bound.
"""
def solution(N, A):
    max_val = curr_max_value = 0
    counters = [0] * N
    
    for i in range(len(A)):
        index = A[i] - 1

        if A[i] == N + 1:
            # set the maximum counter value seen so far
            max_val = curr_max_value
        
        else:
            # set the counter value with the lower bound of max_val
            counters[index] = max(counters[index], max_val) + 1
            curr_max_value = max(curr_max_value, counters[index]) # update the current max value if necessary.
    
    # set all counters that weren't touched to at least max_val
    for i in range(N):
        if counters[i] < max_val: # this counter has not been modified
            counters[i] = max_val

    return counters