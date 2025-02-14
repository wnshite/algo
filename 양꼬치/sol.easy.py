def solution(n, k):
    answer = 0

#             양꼬치총액    음료수총액    서비스음료수가격
    answer = (n * 12000) + (k * 2000) - (n//10 * 2000)

    return answer

print(solution(10, 3))
print(solution(64, 6))