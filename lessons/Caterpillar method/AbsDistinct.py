"""
    Problem description: A non-empty array A consisting of N numbers is given.
    The array is sorted in non-decreasing order.
    The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.
    Problem: Given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.
    Idea: Sort the array by absolute values and traverse it using the caterpillar method.
    Time Complexity: O(n) 
"""
def solution(A):
    n = len(A)

    if n <= 1:
        return n
    
    # sort the array by absolute value
    B = sort_array(A, n)

    total_distinct = 0
    y,i  = 1, 0

    # use the caterpillar method to skip sequences of the same value in sorted A
    while (i < n): # O(n)
        total_distinct += 1
        while (y < n and B[i] == B[y]):
            y += 1

        # advance i to the next unique value in sorted A
        i = max(i + 1, y)

    return total_distinct

""" Helper method """
def sort_array(A, n):
    """
    Sorts an array containing negative numbers followed by positive numbers and sorted in non-descending order.
    Negatives are converted to positives in the result.
    Idea: Find the first positive number and use two pointers to traverse the array in two directions starts from the
    positive number index.
    Time Complexity: O(n) - Using the fact that array A is already sorted we can the sort A by absolute values in O(n)
    """

    first_positive = 0
    sorted_array = []

    # find the first positive integer index in A
    while first_positive < n and A[first_positive] < 0:
        first_positive += 1

    # set two pointers 
    left = first_positive - 1
    right = first_positive

    # traverse from the middle towards the edges and append to the sorted array
    while left >= 0 and right < n:
        if abs(A[left]) < A[right]:
            sort_array.append(abs(A[left]))
            left -= 1
        else:
            sorted_array.append(A[right])
            right += 1
    
    # append remaining negatives
    while left >= 0:
        sorted_array.append(abs(A[left]))
        left -= 1
    
    # append remaining positives
    while right < n:
        sorted_array.append(A[right])
        right += 1

    return sorted_array