def solution(my_string, letter):  # --> 모든 스트링을 한번에...
    answer = ''

    answer = my_string.replace(letter, '')

    return answer

print(solution('asdef', 'f'))
print(solution('BCBdbe', 'B'))