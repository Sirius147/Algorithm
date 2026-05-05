def function():
    # Use a breakpoint in the code line below to debug your script.
    N = int(input())

    # N이하의 자연수를 읽으면서 3, 6, 9 포함 안되어 있으면 출력
    # 자연수를 나머지 연산으로 분리하면서 3,6,9가 포함되어있는지 카운트
    # 3,6,9 개수만큼 -를 출력하기
    for i in range(1, N + 1):
        tmp = i
        cnt = 0
        while tmp != 0:
            m, r = tmp // 10, tmp % 10
            if r in [3, 6, 9]:
                cnt += 1
            tmp = m
        if cnt > 0:
            for _ in range(cnt):
                print("-", end="")
            print(end=" ")
        else:
            print(i, end=" ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()