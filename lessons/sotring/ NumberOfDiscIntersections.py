
def solution(A):

    n = len(A)
    discs_starts_array = [0] * n
    total_intersections = 0

    for i in range(n):
        disc_start = max(0, i - A[i])
        discs_starts_array[disc_start] += 1

    for i in range(1, n):
        discs_starts_array[i] += discs_starts_array[i - 1]

    
    for i in range(n):
        disc_right_index = min(i + A[i], n - 1)
        total_intersections += discs_starts_array[disc_right_index] - (i + 1)

    if total_intersections > 10000000:
        return -1

    return total_intersections

print(solution([1, 5, 2, 1, 4, 0]))