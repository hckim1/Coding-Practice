# 함수 solution은 정수 n을 매개변수로 입력받습니다.
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.


def solution(n):
    # 입력된 정수 n을 문자열로 변환하여 각 자릿수를 리스트에 저장합니다.
    digits = list(str(n))

    # 각 자릿수를 큰 순서대로 정렬합니다.
    digits.sort(reverse=True)
    #오름차순

    # 정렬된 자릿수들을 합쳐서 새로운 정수를 생성합니다.
    new_number = int(''.join(digits))
    # join함수를 통해 문자열 하나로 모으기 -> "873211"
    # 그리구 int()를 씌어 숫자형으로 바꾸어준다 -> 873211

    return new_number


user_input = int(input("정수를 입력하세요: "))  # 사용자로부터 정수 입력 받기
result = solution(user_input)  # solution 함수 호출하여 결과 계산
print(f"정렬된 숫자: {result}")
