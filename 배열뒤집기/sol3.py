def solution(num_list):
    return num_list[ : :-1]   # --> 역순.

    
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))