def function():
    # T 입력 받고 루프 돌기, tc로 출력하기
    # S, K 입력받기
    # 방울이 가운데 시작일 경우 홀수K 일 때 0, 짝수 K일 때 정답은 1
    # 방울이 사이드에 있다면 홀수 K일 때 정답은 1, 짝수 K일 때 정답은 0, 단 오른쪽 사이드에 있었고 K가 0이면 정답은 2
    T = int(input())
    smpl = ["o..", ".o.", "..o"]
    for tc in range(1, T + 1):
        S, K = input().split()
        if S == ".o.":
            if int(K) % 2 == 0:
                print(f"#{tc} 1")
            else:
                print(f"#{tc} 0")
        else:
            if S == "..o" and int(K) == 0:
                print(f"#{tc} 2")
            else:
                if int(K) % 2 == 0:
                    print(f"#{tc} 0")
                else:
                    print(f"#{tc} 1")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()