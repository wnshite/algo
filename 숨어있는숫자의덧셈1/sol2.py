def solution(my_string):
    answer = 0
    numbers = []

    for char in my_string:
        if char.isdigit():
            numbers.append(int(char))

    

    return sum(numbers)

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))