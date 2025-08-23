
def solution(A):

    n = len(A)
    max_peak_left = A[0]
    max_peak_right = 0
    max_value_inA = max(A)
    min_valley = max_value_inA
    max_height = 0

    if n <= 2:
        return 0
    
    i = 1
    if A[0] <= A[1]:
        max_peak_left = A[1]
        i = 2
    if A[n - 1] <= A[n - 2]:
        n -= 1

    while (i < n) :
        if A[i] > A[i - 1]:
            max_height = max(min(max_peak_left, A[i]) - min_valley, max_height)
            max_peak_right = max(max_peak_right, A[i])

        min_valley = min(min_valley, A[i])

        if A[i] >= max_peak_left:
            max_peak_left = A[i]
            max_peak_right = 0
            min_valley = max_value_inA

        i += 1

    return max_height

print(solution([20, 4, 10, 1, 3]))
