
def solution(N):

    min_p, i = 2 * (N + N) , 1 

    while (i * i <= N):
        if (N % i == 0):
            min_p = min(min_p, 2 * ( N // i + i))
        i = i + 1

    return min_p