# 1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될 때까지 다음 작업을 반복하면,
# 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.
#
# 1-1. 입력된 수가 짝수라면 2로 나눕니다.
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
# 예를 들어, 주어진 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 됩니다.
# 위 작업을 몇 번이나 반복해야 하는지 반환하는 함수, solution을 완성해 주세요.
# 단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.

def solution(num):
    # 처음 주어진 num이 1인 경우 바로 0 리턴
    if num == 1:
        return 0

    # 500번 돌리기
    for i in range(500):

        # 짝수라면 2로 나누기
        if num % 2 == 0:
            num = num / 2

        # 홀수라면 3을 곱하고 1을 더하기
        else:
            num = num * 3 + 1

        # 작업을 한 뒤 num이 1인 경우 시행한 횟수 리턴
        if num == 1:
            return i + 1

    # 500번 for문 탈출 시 -1 리턴
    return -1

# 주어진 수 num이 1인 경우, 바로 0을 반환합니다. 이는 주어진 조건에서 명시된 바와 같습니다.
#
# 그렇지 않은 경우, 주어진 수 num을 Collatz 추측에 따라 작업을 반복하는 루프를 최대 500번까지 실행합니다.
# 이 루프에서는 짝수인 경우 2로 나누고, 홀수인 경우 3을 곱하고 1을 더하여 num 값을 갱신합니다.
#
# 루프 내에서 num이 1이 되었을 때, 작업을 수행한 횟수를 반환합니다. i는 0부터 시작하므로 실제 작업 횟수는 i + 1입니다.
#
# 만약 500번의 루프가 실행되었는데도 num이 1이 되지 않은 경우, -1을 반환합니다.
# 이는 주어진 수에 대해 500번까지 시도했음에도 1이 되지 않는 경우를 나타냅니다.
#
# 이렇게 구현된 함수는 주어진 수를 Collatz 추측에 따라 작업을 반복하여 1이 되기까지 걸리는 횟수를 반환하며,
# 작업 횟수가 500번을 넘어가는 경우에는 -1을 반환합니다.