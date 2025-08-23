

# walk: A - 20, S - 30
# scooter: A - 5, S - 40

# ASAASS 
# W = [20, 30, 20, 20, 30, 30] 
# S = [5, 40, 5, 5, 40, 40] 

# W - S = [15, -10, 15, 15, 15, -10, -10]
# PS = [15, 5, 20, 35, 50, 30, 30]
# cost = [30, 15, 25, 10, -5, -20 , 0]
# cost(W-S)_i->n = PS[n - 1] - PS[i - 1] < 0 -> walk the rest of the way, 
def solution(R):

    n = len(R)
    W = [0] * n
    S = [0] * n

    for i in range(n):
        if R[i] == 'A':
            W[i] = 20
            S[i] = 5

        else:
            W[i] = 30
            S[i] = 40

    prefix_sum = [0] * n

    for i in range(n):
        prefix_sum[i] = W[i] - S[i]

    for i in range(1, n):
        prefix_sum[i] += prefix_sum[i - 1]

    cost = [0] * n
    cost[0] = prefix_sum[n - 1]
    for i in range(1,n):
        cost[i] = prefix_sum[n - 1] - prefix_sum[i - 1]

    switch_index = n
    min_val = 0
    for i in range(n):
        if cost[i] < 0:
            if cost[i] < min_val:
                switch_index = i
                min_val = cost[i]
                
    ts = 0
    for i in range(switch_index):
        ts += S[i]

    for i in range(switch_index, n):
        ts += W[i]

    return ts

print(solution("SSSSAAA"))

def cost(scooter, sand):
    costs = [[20, 30], [5, 40]]
    return costs[scooter][sand]


def solution2(R):

    n = len(R)
    foot = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        foot[i] = foot[i + 1] + cost(False, R[i] == 'S')

    ans = foot[0]
    c = 0

    for i in range(n):
        c += cost(True, R[i] == 'S')
        ans = min(ans, foot[i + 1])

    return ans
    
