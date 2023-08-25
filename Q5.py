# 자연수 n이 매개변수로 주어집니다.
# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를
# return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.
#
# 제한사항
# 3 ≤ n ≤ 1,000,000

def solution(n):
    x = n + 1  # n보다 큰 값부터 시작

    while True:
        if x % n == 1:  # x를 n으로 나눈 나머지가 1이면
            return x  # x를 반환
        x += 1  # 다음 숫자로 계속 진행


# 테스트
n = 1
print(solution(n))  # 출력: 4