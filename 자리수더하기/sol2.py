def solution(n):
    answer = 0

    for i in str(n):  # --> for문으로 돌릴 수 있는 건 시퀀스형 데이터만. (ex) n은 안됌. str(n)은 가능.
        answer += int(i)  # --> i 숫자 데이터를 int(i) 시퀀스형 데이터로 변경 후 사용.
    
    return answer

print(solution(1234))
print(solution(930211))