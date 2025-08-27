"""
    Idea: Find the candidate for the dominator: think of it as an elections but for the candidate to win it needs to have
    more then half of the votes - so his votes will cancel all the votes of the other candidates.
    Complexity: O(n)
"""
def solution(A):

    n = len(A)
    size = 0

    # find a candidate for the dominator
    for k in range(n):
        
        if size == 0: # find a new candidate
            size = 1
            value = A[k]
        elif value != A[k]: # cancel the current candidate vote
            size -= 1
        else:
            size += 1 # add one more vote to the current candidate
    
    # return -1 if there is no candidate
    if size == 0:
        return -1
    

    counter = 0

    # count how many times the candidate appears in the array
    for k in range(n):
        if A[k] == value:
            saved = k
            counter += 1
    
    # return the found index if the candidate is a dominator
    if counter > n // 2:
        return saved

    # return -1 if the candidate was not a dominator
    return -1
    
