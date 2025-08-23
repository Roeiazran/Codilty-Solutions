
# 1 partial hour
# few full hours and one partial hour
# few full hours

def solution(E, L):

    e_hour = int(E[0]) * 10 + int(E[1])
    l_hour = int(L[0]) * 10 + int(L[1])

    total_hours = l_hour - e_hour

    e_min = int(E[3]) * 10 + int(E[4])
    l_min = int(L[3]) * 10 + int(L[4])

    if (l_min > e_min) :
        total_hours += 1

    total_fee = 2

    if total_hours:
        total_fee += 3
        total_hours -= 1

    while (total_hours):
        total_fee += 4
        total_hours -= 1

    return total_fee

print(solution("09:42", "09:43"))