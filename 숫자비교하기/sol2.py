def solution(num1, num2):

    if num1 == num2:
        return 1
    else:
        return -1
    

print(solution(2, 3)) # => -1
print(solution(11, 11)) # => 1
print(solution(7, 99)) # => -1