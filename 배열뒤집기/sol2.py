def solution(num_list):
    result = []
    for num in num_list:
        result.insert(0, num)

    return result

    
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))