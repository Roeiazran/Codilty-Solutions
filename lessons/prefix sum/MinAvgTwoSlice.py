
def solution(A):

    n = len(A)
    min_avg = (A[0] + A[1]) / 2
    index = 0

    for i in range(0, n - 2):

        sum_of_two = (A[i] + A[i + 1])
        sum_of_three = sum_of_two + A[i + 2]

        avg_of_two = sum_of_two / 2
        avg_of_three = sum_of_three / 3

        if avg_of_three > avg_of_two:
            if avg_of_two < min_avg:
                index = i
                min_avg = avg_of_two
        else :
            if avg_of_three < min_avg:
                index = i
                min_avg = avg_of_three

    if ((A[n - 1] + A[n - 2]) / 2) < min_avg:
        return n - 2

    return index