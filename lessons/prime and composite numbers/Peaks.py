

def solution(A):

    n = len(A)
    peaks = n * [0]
    if n < 3:
        return 0
    
    for i in range(1, n - 1):
        if A[i] > A[i + 1] and A[i] > A[i - 1]:
            peaks[i] = 1

        peaks[i] += peaks[i - 1]

    peaks[n - 1] = peaks[n - 2]

    num_of_peaks = peaks[n - 1]
    if num_of_peaks == 0:
        return 0
    
    for num_of_blocks in range(num_of_peaks, 1, -1):

        if n % num_of_blocks != 0:
            continue

        block_size = n // num_of_blocks

        start = 0
        end = block_size - 1
        block_found = 0
        while end < n:
            if peaks[end] - peaks[start] == 0:
                break
            block_found += 1
            end += block_size
            start += block_size

        if block_found == num_of_blocks:
            return num_of_blocks
        
    return 1


print(solution([1, 2, 3, 4, 3, 4, 1]))