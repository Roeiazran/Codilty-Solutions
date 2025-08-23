

def solution(X, Y, colors):

    n = len(X)
    raduises = [0] * n

    for i in range(n):
        raduises[i] =  X[i] * X[i]  + Y[i] * Y[i]

    tab = []

    for i in range(n):
        tab.append((raduises[i], colors[i]))

    tab.sort()
    r = g = 0
    max_dots = 0

    for i in range(n):

        if tab[i][1] == 'G':
            g += 1
        else: 
            r += 1

        if r == g and (i == n - 1 or tab[i][0] != tab[i + 1][0]):
            max_dots = r + g
    
    return max_dots

print(solution([1, 0, 0], [0, 1, -1], "GGR"))

    