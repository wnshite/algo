def solution(numbers):
    answer = 0
    
    answer = sum(numbers) / len(numbers)  # len() 은 리스트나 문자열과 같은 시퀀스 자료형의 길이를 반환.
    
    return answer


print(solution([1,2,3,4,5,6,7,8,9,10]))
print(solution([89,90,91,92,93,94,95,96,97,98,99]))