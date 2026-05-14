def function():
    # T 를 입력 받고 루프 생성, #tc로 출력 관리
    # 루프별로 A, B 입력 받고 큰 수와 작은 수의 차이 구하기
    # 해당 값이 1일 경우 불가능
    # 해당 값이 2이상일 때, 2로 나눈 몫이 답, 해당 값이 홀 수 이면 3을 빼고, 2로 나눈 몫 + 1이 답
    T = int(input())
    for tc in range(1, T + 1):
        A, B = map(int, input().split())
        diff = B - A
        if diff == 0:
            print(f"#{tc} 0")
            continue
        if diff <= 1:
            print(f"#{tc} -1")
            continue
        else:
            if diff % 2 == 0:
                print(f"#{tc} {diff // 2}")
            else:
                B -= 3
                diff = B - A
                print(f"#{tc} {(diff // 2) + 1}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()