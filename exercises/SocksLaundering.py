

def solution(K, C, D):

    total_socks = 0
    maxd = max(D)
    maxc = max(C)
    mx = max(maxc, maxd)
    d = len(D)
    c = len(C)

    count_clean = [0] * mx
    count_dirty = [0] * mx

    for i in range(c):
        count_clean[C[i] - 1] += 1

    for i in range(d):
        count_dirty[D[i] - 1] += 1


    for i in range(mx):
        if not K:
            break

        if count_clean[i] % 2 == 1:

            if count_dirty[i]:
                count_dirty[i] -= 1
                count_clean[i] += 1
                K -= 1

    if K > 1:
        for i in range(mx):
            while count_dirty[i] >= 2 and K >= 2:
                count_clean[i] += 2
                count_dirty[i] -= 2
                K -= 2

            if K < 2:
                break
    
    for i in range(mx):
        total_socks += (count_clean[i] // 2)

    return total_socks


print(solution(5, [1, 1, 3, 4], [3, 3, 3, 5]))