
def solution(N):
    
    i, dev = 1, 0
    while (i * i < N):
        if (N % i) == 0:
            dev += 2
        i += 1
    if (i * i == N):
        dev += 1

    return dev

