

def solution(A):

    def merge_sort(A):

        n = len(A)
        if n <= 1:
            return 0, A
        
        mid = n // 2

        inv_left, left = merge_sort(A[:mid])
        inv_right, right = merge_sort(A[mid:])
        inv_split, merged = merge(left, right)

        return inv_left + inv_right + inv_split, merged

    def merge(left, right):
        i = j = 0
        inv_count = 0
        merged = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else: 
                merged.append(right[j])
                inv_count += len(left) - i
                j += 1

        merged += left[i:]
        merged += right[j:]

        return inv_count, merged
    
    inv_count,_ = merge_sort(A)

    if inv_count > 1000000000:
        return -1
    return inv_count

print(solution([-1, 6, 3, 4, 7, 4]))