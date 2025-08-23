import math
def solution(A):

    n ,j = len(A), 0
    peaks = []
    for i in range(1, n - 1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            peaks.append(i)
            j += 1

    if (j <= 1):
        return j

    max_flags, flags_set = min(math.ceil(math.sqrt(peaks[j - 1] - peaks[0])), j) + 1, 2

    for flags in range(max_flags, 1, -1):

        flags_set = 2
        start_peak = peaks[0]
        end_peak = peaks[j - 1]
        start, end = 0, j - 1
    #[1 ,3 ,5]
        while (start < end):
            start += 1
            end -= 1

            if (flags_set == flags):
                return flags
 
            if (peaks[start] - flags >= start_peak) and (peaks[start] + flags <= end_peak):
                flags_set += 1
                start_peak = peaks[start]
                
            if (peaks[end] + flags <= end_peak) and (peaks[end] - flags >= start_peak):
                flags_set += 1
                end_peak = peaks[end]

            if (flags_set == flags):
                return flags      
    return 0

print(solution([1, 5, 3, 4, 3, 6, 4])) # hits first condition
print(solution([1, 10, 1, 1, 1, 1, 10, 1, 1, 1, 1, 10, 1, 1, 1, 1, 10, 1, 1, 1, 1, 10, 1])) # hits second condition

def solution(A):

    n ,j = len(A), 0
    peaks = []
    for i in range(1, n - 1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            peaks.append(i)
            j += 1

    if (j <= 1):
        return j
    
    # [1, 3, 5] 
    # mf = min(3, 3) - 3
    # k = 3, c = 2 #
    max_flags = min (j, int(len(A) ** 0.5)) + 1
    max_flags_set = 0
    for k in range(max_flags, 1, -1):
        lastF = 0
        c = 1

        for i in range(1, j):
            if peaks[i] - peaks[lastF] >= k and c < k:
                c += 1
                lastF = i

        if c < max_flags_set: return max_flags_set
        elif max_flags_set < c: max_flags_set = c

    pass
    
print(solution([1, 5, 3, 4, 3, 6, 4])) # hits first condition#
print(solution([1, 10, 1, 1, 1, 1, 10, 1, 1, 1, 1, 10, 1, 1, 1, 1, 10, 1, 1, 1, 1, 10, 1])) # hits second condition3
