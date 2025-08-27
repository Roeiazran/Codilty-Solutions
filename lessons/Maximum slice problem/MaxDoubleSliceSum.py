"""
    Idea: Finding a double slice is basically finding a left right and middle indices such that sum between them is the
    largest. For each index calculate the maximum sum that can summed from array A coming from any direction, now the index 
    who has the largest sum, say coming from the left, it id the wanted left index. 
    Iterate over any index and consider it as a candidate for the middle index by checking his max left and right sums.
    Complexity: O(n)
"""
def solution(A):

    N = len(A)

    # initialize the left and right max sums array
    l = [0] * N
    r = [0] * N

    # set to zero for excluding the edges of array A
    l[0] = 0
    r[N - 1] = 0

    # calculate the maximum sum at any index coming from left to right
    for i in range(1, N):
        l[i] = max(0, l[i - 1] + A[i])

    for i in range(N - 2, -1, -1):
        r[i] = max(0, r[i + 1] + A[i])

    m = 0
    # consider any index as the middle index
    for i in range(1, N - 1):
        m = max(m, l[i - 1] + r[i + 1])

    return m