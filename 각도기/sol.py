def solution(angle):
    answer = 0

    if angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle < 180:
        return 3
    else:
        return 4
    
    return answer

print(solution(80))
print(solution(11))
print(solution(280))