def solution(my_string):
    answer = 0

    for char in my_string:
        try:
            answer += int(char)
        except:
            continue

    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))