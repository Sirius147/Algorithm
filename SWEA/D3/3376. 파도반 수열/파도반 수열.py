def function():
    # T 입력 받고 루프 생성 tc로 출력 번호
    # 사이즈 101의 리스트 생성
    # 초기데이터 5개 넣기 (0, 1,1,1,2,2)
    # 이후 데이터는 dp[i] = dp[i-1] + dp[i-5], 인덱스 시작은 6부터 N까지
    # p[N] 출력

    T = int(input())
    for tc in range(1, T + 1):
        p = [0 for _ in range(101)]
        p[0], p[1], p[2], p[3], p[4], p[5] = 0, 1, 1, 1, 2, 2
        for i in range(6, len(p)):
            p[i] = p[i - 1] + p[i - 5]
        N = int(input())
        print(f"#{tc} {p[N]}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function()
