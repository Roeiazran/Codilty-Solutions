

def sort_array(A, n):

    first_positive = 0
    sorted_array = [0] * n

    for i in range(1, n):
        if A[i - 1] < 0 and A[i] >= 0:
            first_positive = i
            break
    
    if first_positive == 0:
        for i in range(n):
            sorted_array[i] = abs(A[n - 1 - i])
        return sorted_array
    
    left = first_positive - 1
    right = first_positive + 1
    sorted_array[0] = A[first_positive]
    ind = 1
    while (left >= 0 and right < n):
        if abs(A[left]) < A[right]:
            sorted_array[ind] = abs(A[left])
            left -= 1
        else:
            sorted_array[ind] = A[right]
            right += 1
        ind += 1

    while (left >= 0):
        sorted_array[ind] = abs(A[left])
        left -= 1
        ind += 1
    
    while (right < n):
        sorted_array[ind] = A[right]
        right += 1
        ind += 1

    return sorted_array

def solution(A):
    n = len(A)

    if n <= 1:
        return n
    B = abs(A)
    print(B)
    
    B = sort_array(A, n)
    total_distinct = 0

    y,i  = 1, 0
    while (i < n): # O(n)
        total_distinct += 1
        while (y < n and B[i] == B[y]):
            y += 1

        i = max(i + 1, y)

    return total_distinct

print(solution([-20, -5 ,5, 10, 10, 20, 30]))