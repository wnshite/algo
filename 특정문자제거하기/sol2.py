def solution(my_string, letter): # --> 특정문자가 아닌 것을 지우기
    answer = ''
    
    for char in my_string:
        if char != letter:
            answer = answer + char


    return answer

print(solution('asdef', 'f'))
print(solution('BCBdbe', 'B'))