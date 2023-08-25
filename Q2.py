# 평균 구하기
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
#
# 제한사항
# arr은 길이 1 이상, 100 이하인 배열입니다.
# arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

def solution(arr):
    result = sum(arr) / len(arr)
    return result

# 사용자로부터 숫자들을 공백으로 구분하여 입력 받기
user_input = input("숫자들을 공백으로 구분하여 입력하세요: ")
try:
    # 입력 받은 값을 공백을 기준으로 분리하여 각 숫자들을 정수로 변환하고, 리스트로 저장합니다.
    num_list = [int(num) for num in user_input.split()]

    # 리스트의 평균값을 계산하고 출력
    result = solution(num_list)
    print(f'{result:.2f}')

except ValueError:
    print("유효한 숫자를 입력하시오.")