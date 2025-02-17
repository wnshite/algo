def solution(n, k):
    answer = 0
    yang = n
    drink = k

    if n >= 10:
        service = n // 10
        answer = n * 12000 + (k-service) * 2000
    else:
        answer = n * 12000 + k * 2000

    return answer

print(solution(10, 3))
print(solution(64, 6))