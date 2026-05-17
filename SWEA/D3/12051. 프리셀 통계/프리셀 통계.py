def function():
    # T값 입력 받고 루프 생성, #tc별로 출력, Possible/Broken
    # N, pd, pg 별로 입력 받기
    # N이 100이상이면 첫 조건 성립, 100아래이면 루프를 돌며 pd와 곱했을 때 100으로 나누어떨어지면 통과 실패 시 Broken
    # pg가 0 또는 100일 때 pd가 0 또는 100이 아니었으면 브로큰 이외는 Possible
    T = int(input())
    for tc in range(1, T + 1):
        N, pd, pg = map(int, input().split())
        if pg == 100 and pd != 100:
            print(f"#{tc} Broken")
            continue
        if pg == 0 and pd != 0:
            print(f"#{tc} Broken")
            continue
        if N >= 100:
            print(f"#{tc} Possible")
        else:
            flag = False
            for n in range(1, N + 1):
                if (n * pd) % 100 == 0:
                    print(f"#{tc} Possible")
                    flag = True
                    break
            if flag:
                continue
            print(f"#{tc} Broken")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()